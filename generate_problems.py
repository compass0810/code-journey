"""
generate_problems.py - Qwen2.5 14B を使って演習問題を自動生成し problems_data.js に書き込むスクリプト

使い方:
  # 特定のパスに問題を生成
  python generate_problems.py --path "math/math_1/numbers_and_expressions/calculation" --count 5

  # 設定ファイルで一括生成（周回モード）
  python generate_problems.py --batch config.json

  # 全ての空パスに自動生成
  python generate_problems.py --auto --count 3

必要環境:
  - Python 3.8+
  - pip install requests
  - Ollama が localhost:11434 で起動中、qwen2.5:14b モデルがプルされていること
"""

import json
import re
import sys
import os
import argparse
import time
import subprocess
from datetime import datetime
import random

# 教科・科目の日本語表示名マッピング
SUBJECT_DISPLAY_MAP = {
    "math/math_1": "数学I",
    "math/math_a": "数学A",
    "math/math_2": "数学II",
    "math/math_b": "数学B",
    "math/math_3": "数学III",
    "math/math_c": "数学C",
    "english/short_fill": "英語（短文補充）",
    "english/long_reading": "英語（長文読解）",
    "english/translation_ej": "英語（英文和訳）",
    "english/translation_je": "英語（和文英訳）"
}

def parse_data_js_content(content: str):
    """data.js から JSON 部分を抽出して dict を返す"""
    match = re.search(r'window\.practiceData\["?[^"]+"?\]\s*=\s*(\{[\s\S]*\});?\s*$', content)
    if not match:
        return None
    js_obj = match.group(1)
    try:
        return json.loads(js_obj)
    except json.JSONDecodeError:
        fixed = re.sub(r'(\w+)\s*:', r'"\1":', js_obj)
        try:
            return json.loads(fixed)
        except Exception:
            return None


def get_next_serial_number(subject_display):
    """全 data.js を走査して、指定科目の次の通し番号を返す"""
    max_no = 0
    for root, _, files in os.walk(PROBLEMS_DIR):
        if "data.js" not in files:
            continue
        file_path = os.path.join(root, "data.js")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = parse_data_js_content(f.read())
            if not data:
                continue
            for chapter in data.get("chapters", []):
                for lesson in chapter.get("lessons", []):
                    sn = lesson.get("serial_number", "")
                    # subject_displayが含まれていない古いデータも拾えるように、前方一致で判定
                    if not sn.startswith(subject_display):
                        continue
                    match = re.search(r"No\.(\d+)", sn)
                    if match:
                        max_no = max(max_no, int(match.group(1)))
        except Exception:
            continue
    return f"{subject_display} No.{max_no + 1}"
import uuid
import requests
try:
    import google.generativeai as genai
    HAS_GEMINI = True
except ImportError:
    HAS_GEMINI = False

# ============================================================
# 設定
# ============================================================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma4:e4b"
GEMINI_API_KEY = "AIzaSyDWECPPrJ3tXKxxJ0AMFKPyBadBzTVJl04"  # 環境変数から取得
GEMINI_MODEL_NAME = "gemini-3.1-flash-lite"  # 最新の Gemma 4 31B モデルを指定

if HAS_GEMINI and GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

PROBLEMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "problems")

# パスからプロンプトのヒントを自動推定するためのマッピング
SUBJECT_HINTS = {
    "english/short_fill": {
        "subject": "英語",
        "type": "短文空欄補充",
        "prompt_template": """あなたは熟練した英語教師です。以下の条件で英語の短文穴埋め問題（4択形式）を{count}問作成してください。

トピック: {topic}
レベル: {level}

## 今回のターゲット文法事項【必須・抽選結果】
以下の文法事項を問題のターゲットとすること。この文法事項の正しい使い方を問う問題を作成してください：
{selected_grammar}
- chapterフィールドには上記の文法事項名をそのまま記入すること（複数の場合は「・」で区切る）
- **強調構文（It is ... that ~）が上記に含まれていない限り、強調構文を使わないこと**

【品質指示】
- テーマは日常会話、ビジネス、科学、歴史、心理学、環境問題、芸術など、知的で実用的な文脈を選ぶこと
- 選択肢は文法的に誤りやすい紛らわしいものを含めること
- 英文は自然で試験問題として成立すること

以下のJSON配列として出力してください（余計な説明は不要、JSONのみ）:
[
  {{
    "title": "問題の短いタイトル",
    "instruction": "空欄に入る最も適切なものを選択肢から選んでください。",
    "content": "英文 (例: Despite the ___ traffic, we arrived on time.)",
    "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4"],
    "answers": ["正解の単語"],
    "chapter": "使用した文法事項名"
  }}
]"""
    },
    "english/long_reading": {
        "subject": "英語",
        "type": "長文読解",
        "prompt_template": """あなたは熟練した英語教師です。以下の条件で英語の長文読解問題を{count}問作成してください。

トピック: {topic}
レベル: {level}

## 今回のターゲット文法事項【必須・抽選結果】
英文パッセージの中に以下の文法構造を自然な形で含めること：
{selected_grammar}
- chapterフィールドにはこの文法事項名を記入すること（複数の場合は「・」で区切る）
- **強調構文（It is ... that ~）が上記に含まれていない限り、強調構文を使わないこと**

【品質指示】
- テーマはAI技術・歴史・心理学・環境・異文化など、ジャンルを大きく散らすこと
- 意見対立・最新の発見・意外な事実など、読んでいて興味深い内容にすること
- 文章の長さはレベルに合わせて3〜8文程度とし、論理的な構造を持たせること
- 質問は筆者の意図・代名詞の指示内容・未知語の推測など、深い理解を要するものにすること
- 回答は短い英語フレーズまたは1文で答えられるものにすること

以下のJSON配列として出力してください:
[
  {{
    "title": "長文タイトル",
    "instruction": "以下の文章を読んで質問に答えてください。\\n\\n[英文]\\n...\\n\\n質問: ...",
    "answers": ["標準的な正解", "許容される別解"],
    "chapter": "使用した文法事項名"
  }}
]"""
    },
    "english/translation_ej": {
        "subject": "英語",
        "type": "英文和訳",
        "prompt_template": """あなたは熟練した英語教師です。以下の条件で「英文和訳」問題を{count}問作成してください。

トピック: {topic}
レベル: {level}

## 今回のターゲット文法事項【必須・抽選結果】
英文に以下の文法構造を**必ず含めること**：
{selected_grammar}
- 上記の文法事項が和訳の最大のポイントとなるよう英文を設計すること
- chapterフィールドにはこの文法事項名を記入すること（複数の場合は「・」で区切る）
- **強調構文（It is ... that ~）が上記に含まれていない限り、強調構文を使わないこと**

【品質指示】
- テーマは文学的表現・テクノロジー・格言・ニュース・哲学的考察など全く異なる分野から選ぶこと
- 「私」「彼」を主語にしたありきたりな日常文は避け、「訳しにくい」が自然な英文を生成すること

以下のJSON配列として出力してください:
[
  {{
    "title": "英文和訳 (テーマ)",
    "instruction": "次の英文を日本語に訳してください。",
    "content": "英文",
    "answers": ["自然な日本語訳", "直訳に近いが正しい訳"],
    "chapter": "使用した文法事項名"
  }}
]"""
    },
    "english/translation_je": {
        "subject": "英語",
        "type": "和文英訳",
        "prompt_template": """あなたは熟練した英語教師です。以下の条件で「和文英訳（英作文）」問題を{count}問作成してください。

トピック: {topic}
レベル: {level}

## 今回のターゲット文法事項【必須・抽選結果】
以下の文法事項を英訳で表現させる問題を作成すること：
{selected_grammar}
- 日本語文は上記の文法事項を使った英訳が自然になるよう設計すること
- chapterフィールドにはこの文法事項名を記入すること（複数の場合は「・」で区切る）
- **強調構文（It is ... that ~）が上記に含まれていない限り、強調構文を使わないこと**

【品質指示】
- シチュエーションはビジネス・科学ニュース・歴史・感情表現など、毎回全く異なる分野から選ぶこと
- 日本人が直訳しがちな表現を含め、自然な英語への変換力を問う問題にすること
- 「私は昨日図書館に行きました」のような単調な文は避け、少し複雑で知的な日本語文を提示すること

以下のJSON配列として出力してください:
[
  {{
    "title": "和文英訳 (テーマ)",
    "instruction": "次の日本語を英語に直してください。",
    "content": "日本語の文章",
    "answers": ["標準的な英文解答", "別の正しい表現"],
    "chapter": "使用した文法事項名"
  }}
]"""
    },
    "math": {
        "subject": "数学",
        "type": "計算・証明",
        "prompt_template": """あなたは数学教師です。以下の条件で数学の演習問題を{count}問作成してください。

科目・単元: {topic}
レベル: {level}

【重要指示】
- レベルD以外では、その単元を学ぶ上で必要な前提知識（例：2次関数なら数と式の展開など）を除き、他の単元の知識（例：数Iの範囲なのに微分を使う、ベクトルを使うなど）を要求しないでください。
- 答えは数値や式を短く入力する形式（1行）で答えてください。
- 答えの表記は統一してください（例: 分数は「3/4」、座標は「(2,-1)」、式は「x^2+3x+2」など）。

以下のJSON配列として出力してください（余計な説明は不要、JSONのみ）:
[
  {{
    "title": "問題の短いタイトル",
    "instruction": "問題文（数式はx^2のように表記、改行は\\nを使用）",
    "answers": ["正解"],
    "chapter": "単元カテゴリ名"
  }}
]"""
    }
}

# 表示用の日本語マッピング
DISPLAY_NAME_MAP = {
    "english": "英語",
    "math": "数学",
    "short_fill": "短文空欄補充",
    "long_reading": "長文読解",
    "translation_ej": "英文和訳",
    "translation_je": "和文英訳",
    "math_1": "数学I",
    "math_a": "数学A",
    "math_2": "数学II",
    "math_b": "数学B",
    "math_3": "数学III",
    "math_c": "数学C",
    "numbers_and_expressions": "数と式",
    "calculation": "式の計算",
    "real_numbers": "実数",
    "inequalities": "1次不等式",
    "logic_and_sets": "集合と論証",
    "sets": "集合",
    "logic": "命題と論証",
    "quadratics": "2次関数",
    "graph": "関数とグラフ",
    "equations_inequalities": "2次方程式・2次不等式",
    "trigonometry": "図形と計量（三角比）",
    "acute": "鋭角の三角比",
    "extension": "三角比の拡張",
    "application": "三角形への応用",
    "data_analysis": "データの分析",
    "variance": "データの散らばりの大きさ",
    "correlation": "データの相関",
    "probability": "場合の数と確率",
    "counts": "場合の数",
    "basics": "基本性質",
    "various": "いろいろな事象",
    "geometry": "図形の性質",
    "triangles": "三角形の性質",
    "circles": "円の性質",
    "solid": "空間図形",
    "human_activity": "数学と人間の活動",
    "living": "社会生活",
    "enjoying": "数学的な表現",
    "equations_proof": "式と証明",
    "higher": "高次方程式",
    "proof": "証明",
    "coordinates": "図形と方程式",
    "lines": "直線",
    "loci": "軌跡と領域",
    "functions": "関数",
    "addition": "加法定理",
    "exponential_log": "指数関数・対数関数",
    "exponential": "指数関数",
    "logarithmic": "対数関数",
    "calculus": "微分法・積分法",
    "differentiation": "微分法",
    "integration": "積分法",
    "sequences": "数列",
    "induction": "数学的帰納法",
    "statistics": "統計的な推測",
    "sampling": "標本調査",
    "distribution": "確率分布",
    "normal": "正規分布",
    "inference": "統計的推定",
    "society": "数学と社会生活",
    "phenomena": "数学的な諸現象",
    "functions_limits": "極限",
    "sequence_limits": "数列の極限",
    "function_limits": "関数の極限",
    "differentiation_apps": "微分法の応用",
    "increase_decrease": "増減とグラフ",
    "integration_apps": "積分法の応用",
    "vectors": "ベクトル",
    "plane": "平面ベクトル",
    "space": "空間ベクトル",
    "curves": "曲線",
    "quadrics": "2次曲線",
    "polar": "極座標",
    "complex_plane": "複素数平面",
    "representation": "データの表現",
    "matrices": "行列",
    "data": "データ処理",
    "level_A": "レベルA（基本・標準）",
    "level_B": "レベルB（発展）",
    "level_C": "レベルC（共通テスト）",
    "level_D": "レベルD（二次試験）"
}

# ============================================================
# 英語文法事項一覧（抽選→制約付き生成システム用）
# BASE_WEIGHT: 高いほど選ばれやすい（強調構文は意図的に1=最低）
# ============================================================
ENGLISH_GRAMMAR_LIST = {
    # ── 動詞・時制 ──
    "現在完了（経験・継続・完了）": 5,
    "過去完了": 5,
    "未来完了": 4,
    "時制の一致": 5,
    "仮定法過去": 6,
    "仮定法過去完了": 6,
    "混合仮定法": 4,
    "wish / as if の仮定法": 4,
    "使役動詞（make/let/have/get）": 5,
    "知覚動詞": 4,
    "助動詞の過去形（would/could/might）": 5,
    "助動詞＋完了形（should have done 等）": 5,
    "受動態（進行形・完了形）": 4,
    "二重目的語・第5文型": 4,
    # ── 関係詞 ──
    "関係代名詞（制限用法）": 4,
    "関係代名詞（継続用法）": 5,
    "関係副詞（where/when/why/how）": 5,
    "複合関係詞（whoever/whatever 等）": 4,
    "前置詞＋関係代名詞": 5,
    "関係代名詞 what": 5,
    # ── 不定詞・動名詞・分詞 ──
    "不定詞の副詞的用法（結果・条件）": 5,
    "不定詞の意味上の主語（for / of to V）": 5,
    "原形不定詞（使役・知覚）": 4,
    "動名詞の意味上の主語": 4,
    "完了動名詞（having done）": 4,
    "分詞構文": 5,
    "独立分詞構文": 5,
    "付帯状況の with": 4,
    # ── 比較 ──
    "原級比較（as ... as）": 4,
    "比較級の強調（much/far/even）": 5,
    "比較を使った最上級表現": 4,
    "倍数表現": 4,
    "差の比較": 4,
    # ── 倒置・省略・強調 ──
    "否定の倒置（Never/Hardly/Seldom 等）": 5,
    "条件節の倒置（Were it not for 等）": 4,
    "省略（as/than 節）": 3,
    "強調構文（It is ... that ~）": 1,  # 補助的要素に格下げ
    "do 強調": 3,
    # ── 接続詞・前置詞 ──
    "譲歩節（although/even though/while）": 5,
    "様態節（as/as if）": 4,
    "目的節（so that/in order that）": 4,
    "結果節（so ... that / such ... that）": 5,
    "時間節（as soon as/by the time 等）": 4,
    "条件節（unless/provided that/as long as）": 5,
    # ── 特殊構文・語法 ──
    "無生物主語": 6,
    "形式主語 it（It is ... that/to）": 4,
    "形式目的語 it（find it ... to/that）": 4,
    "部分否定": 5,
    "二重否定": 3,
    "否定の強調（by no means / far from 等）": 4,
    # ── イディオム・コロケーション ──
    "動詞句イディオム": 4,
    "形容詞＋前置詞のコロケーション": 4,
    "同格の that": 5,
    "名詞節（that 節・wh 節）": 4,
    "挿入句・独立構文": 3,
}

# レベル別の文法事項抽選個数範囲 {level_key: (min, max)}
LEVEL_GRAMMAR_COUNT = {
    "level_A": (1, 1),
    "level_B": (1, 2),
    "level_C": (2, 3),
    "level_D": (3, 3),
}

# 文法使用履歴ファイルパス
GRAMMAR_HISTORY_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "grammar_history.json"
)


class GrammarSelector:
    """使用履歴に基づく重み付き文法事項抽選クラス"""

    def __init__(self):
        self.history = self._load_history()

    def _load_history(self) -> dict:
        if os.path.exists(GRAMMAR_HISTORY_FILE):
            try:
                with open(GRAMMAR_HISTORY_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def _save_history(self):
        with open(GRAMMAR_HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    def _effective_weight(self, item: str) -> float:
        """使用回数ペナルティ込みの実効重みを返す"""
        base = ENGLISH_GRAMMAR_LIST[item]
        usage = self.history.get(item, 0)
        return base / (1.0 + usage * 0.4)

    def select_items(self, n: int) -> list:
        """n個の文法事項を重み付きランダムで重複なく選ぶ"""
        items = list(ENGLISH_GRAMMAR_LIST.keys())
        weights = [self._effective_weight(item) for item in items]
        selected = []
        rem_items = items[:]
        rem_weights = weights[:]
        for _ in range(min(n, len(items))):
            chosen = random.choices(rem_items, weights=rem_weights, k=1)[0]
            selected.append(chosen)
            idx = rem_items.index(chosen)
            rem_items.pop(idx)
            rem_weights.pop(idx)
        return selected

    def record_usage(self, items: list):
        """使用した文法事項のカウントを+1して保存"""
        for item in items:
            self.history[item] = self.history.get(item, 0) + 1
        self._save_history()

    @staticmethod
    def get_count_for_level(path: str) -> int:
        """パスのレベルに応じた抽選個数をランダムで返す"""
        for level_key, (mn, mx) in LEVEL_GRAMMAR_COUNT.items():
            if level_key in path:
                return random.randint(mn, mx)
        return 2  # デフォルト


def to_display_name(slug):
    """内部IDを表示用の日本語に変換する"""
    if not slug: return ""
    # スラッシュ区切りの場合は各要素を変換
    if "/" in slug:
        return " / ".join([DISPLAY_NAME_MAP.get(s, s) for s in slug.split("/")])
    return DISPLAY_NAME_MAP.get(slug, slug)

# ============================================================
# ユーティリティ
# ============================================================

def get_available_paths():
    """problems フォルダを走査して既存の data.js パス一覧を返す"""
    paths = []
    for root, _, files in os.walk(PROBLEMS_DIR):
        if "data.js" not in files:
            continue
        rel_path = os.path.relpath(root, PROBLEMS_DIR).replace("\\", "/")
        paths.append(rel_path)
    return sorted(paths)

def load_problems_for_path(path: str):
    """指定パスのデータを読み込む（新形式のフォルダ内data.jsと、旧形式のファイルを両方チェックする）"""
    # 1. 新形式: problems/{path}/data.js
    file_path = os.path.join(PROBLEMS_DIR, path, "data.js")
    if not os.path.exists(file_path):
        # 2. 旧形式: problems/{path}.js
        file_path = os.path.join(PROBLEMS_DIR, f"{path}.js")
        
    if not os.path.exists(file_path):
        return {"chapters": []}

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    data = parse_data_js_content(content)
    if not data:
        return {"chapters": []}
    return data


def save_problems_data(path: str, data: dict):
    """個別のパスにデータを書き出し、index.js を更新する（フォルダ内の data.js に保存）"""
    # フォルダを作成
    dir_path = os.path.join(PROBLEMS_DIR, path)
    os.makedirs(dir_path, exist_ok=True)
    
    file_path = os.path.join(dir_path, "data.js")
    
    json_str = json.dumps(data, ensure_ascii=False, indent=4)

    content = f"""// Auto-generated problem data
window.practiceData = window.practiceData || {{}};
window.practiceData["{path}"] = {json_str};
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Update index.js
    available_paths = set(get_available_paths())
    available_paths.add(path)
    
    index_path = os.path.join(PROBLEMS_DIR, "index.js")
    paths_json = json.dumps(sorted(list(available_paths)), ensure_ascii=False, indent=4)
    index_code = f"""// Auto-generated problem paths
const availablePracticePaths = {paths_json};
"""
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_code)

    print(f"[OK] {file_path} に保存しました。")


def get_prompt_info(path: str):
    """パスから適切なプロンプトテンプレートとメタ情報を推定する"""
    parts = path.split("/")

    # レベル推定
    is_prob = any(p in path for p in ["probability", "counts", "statistics"])
    
    level_desc = "標準"
    is_english = "english" in path
    
    for p in parts:
        if "level_A" in p or "level_a" in p.lower():
            if is_english:
                level_desc = "レベルA: 基本的な語彙と文法。中学〜高校初級レベル。日常的な表現。"
            else:
                level_desc = "レベルA: 単純計算、公式の適用（例：微分係数を求めるだけ、展開公式をそのまま使うなど）"
        elif "level_B" in p or "level_b" in p.lower():
            if is_english:
                level_desc = "レベルB: 高校標準レベル。少し複雑な構文（関係代名詞、分詞構文など）や共通テストレベルの語彙。"
            else:
                level_desc = "レベルB: 応用問題、複合的な計算（例：接線と法線の交点を求める、文章から立式するなど）"
        elif "level_C" in p or "level_c" in p.lower():
            if is_english:
                level_desc = "レベルC: 大学入試レベル。抽象度の高い内容、複雑な論理構造、高度な語彙。"
            elif is_prob:
                level_desc = "レベルC: 複数の条件が組み合わさった応用問題。計算量は多いが、具体的な数値を用いてください（文字定数nなどは使わない）。"
            else:
                level_desc = "レベルC: パラメータを含む問題、文字定数を含む関数（例：定数aを含む2次関数の接線が特定の点を通る条件を求めるなど）"
        elif "level_D" in p or "level_d" in p.lower():
            if is_english:
                level_desc = "レベルD: 難関国立・私立大の二次試験レベル。非常に高度な語彙、難解な英文解釈、背景知識を要する論説文など。"
            else:
                level_desc = """レベルD: 難関大（旧帝大・早慶等）の入試二次試験レベル。
- 単なる連立方程式の計算で終わるような問題は避け、深い考察、論証のステップ、または複数の条件を組み合わせた複雑な思考力を要する問題にしてください。
- 【重要】「定数を決定せよ」という問いに対して、条件が不足して一意に定まらないようなミスを絶対にしないでください。
- 最終的な答えは必ず「数値」や「文字式による範囲（a > 1/2など）」のように、1行で簡潔に答えられる形に落とし込んでください。"""

    # トピック推定: パスの各セグメントを連結（レベル部分を除く）
    topic_parts = [p for p in parts if not p.startswith("level_")]
    topic = " / ".join(topic_parts)

    # プロンプトテンプレート選択
    for prefix, info in SUBJECT_HINTS.items():
        if path.startswith(prefix):
            return info["prompt_template"], topic, level_desc

    # デフォルト: 数学
    if path.startswith("math"):
        return SUBJECT_HINTS["math"]["prompt_template"], topic, level_desc

    # その他
    return SUBJECT_HINTS["math"]["prompt_template"], topic, level_desc


def call_gemini(prompt: str, max_retries: int = 3) -> str:
    """Gemini APIを呼び出してレスポンステキストを返す"""
    global GEMINI_API_KEY
    if not HAS_GEMINI:
        print("[ERROR] google-generativeai がインストールされていません。")
        return ""
    
    # APIキーが未設定の場合は入力を求める
    if not GEMINI_API_KEY:
        print("\n" + "!"*60)
        print(" Gemini APIキーが設定されていません。")
        print(" https://aistudio.google.com/app/apikey で取得したキーを入力してください。")
        print("!"*60)
        key = input("APIキーを入力: ").strip()
        if not key:
            print("[ERROR] キーが入力されなかったため、生成を中止します。")
            return ""
        GEMINI_API_KEY = key
        genai.configure(api_key=GEMINI_API_KEY)

    model = genai.GenerativeModel(GEMINI_MODEL_NAME)
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            if response.text:
                return response.text
        except Exception as e:
            print(f"\n  [WARN] Gemini APIエラー: {e} (リトライ {attempt+1}/{max_retries})")
            time.sleep(1)
    return ""


def call_llm(prompt: str, engine: str = "ollama") -> str:
    """指定されたエンジンでLLMを呼び出す"""
    if engine == "gemini":
        return call_gemini(prompt)
    else:
        return call_ollama(prompt)


def call_ollama(prompt: str, max_retries: int = 3) -> str:
    """Ollama APIを呼び出してレスポンステキストを返す"""
    for attempt in range(max_retries):
        try:
            resp = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "num_predict": 4096,
                    }
                },
                timeout=300
            )
            resp.raise_for_status()
            return resp.json()["response"]
        except requests.exceptions.ConnectionError:
            print(f"[ERROR] Ollama に接続できません ({OLLAMA_URL})。Ollama が起動していることを確認してください。")
            if attempt < max_retries - 1:
                print(f"  {5*(attempt+1)}秒後にリトライします...")
                time.sleep(5 * (attempt + 1))
            else:
                raise
        except Exception as e:
            print(f"[ERROR] API呼び出しエラー (attempt {attempt+1}): {e}")
            if attempt < max_retries - 1:
                time.sleep(3)
            else:
                raise


def parse_llm_response(response_text: str) -> list:
    """LLMのレスポンスからJSON配列を抽出する"""
    # コードブロック内のJSONを探す
    code_match = re.search(r"```(?:json)?\s*\n?([\s\S]*?)\n?```", response_text)
    if code_match:
        json_str = code_match.group(1).strip()
    else:
        # コードブロックなし: JSON配列を直接探す
        arr_match = re.search(r"\[[\s\S]*\]", response_text)
        if arr_match:
            json_str = arr_match.group(0)
        else:
            print("[WARN] LLMレスポンスからJSONを抽出できませんでした。")
            print("  レスポンス:", response_text[:500])
            return []

    try:
        problems = json.loads(json_str)
        if isinstance(problems, list):
            return problems
        print("[WARN] JSONは配列ではありません。")
        return []
    except json.JSONDecodeError as e:
        print(f"[WARN] JSONパースエラー: {e}")
        print("  抽出テキスト:", json_str[:300])
        return []


def get_default_difficulty(path: str) -> float:
    """パス文字列からデフォルト難易度定数を返す"""
    if "level_A" in path:
        return 2.0
    if "level_B" in path:
        return 5.0
    if "level_C" in path:
        return 7.5
    if "level_D" in path:
        return 10.0
    return 5.0


def generate_ids(path: str, count: int) -> list:
    """ユニークなIDリストを生成する"""
    prefix = path.replace("/", "-")
    return [f"{prefix}-{str(uuid.uuid4())}" for _ in range(count)]


def merge_problems(existing_data: dict, path: str, new_problems: list) -> dict:
    """新しい問題を既存データにマージする"""
    if "chapters" not in existing_data:
        existing_data["chapters"] = []

    chapters = existing_data["chapters"]

    # chapterごとにグルーピング
    chapter_map = {}
    for ch in chapters:
        chapter_map[ch["title"]] = ch

    ids = generate_ids(path, len(new_problems))

    parts = path.split("/")
    subject_key = "/".join(parts[:2])
    subject_display = SUBJECT_DISPLAY_MAP.get(subject_key, "その他")
    next_serial = get_next_serial_number(subject_display)
    match = re.search(r"No\.(\d+)", next_serial)
    next_no = int(match.group(1)) if match else 1
    default_difficulty = get_default_difficulty(path)

    for i, prob in enumerate(new_problems):
        serial_number = f"{subject_display} No.{next_no}"
        next_no += 1
        
        chapter_title = prob.get("chapter", "その他")
        lesson = {
            "id": ids[i],
            "serial_number": serial_number,
            "subject_display": subject_display,
            "difficulty": default_difficulty,
            "title": prob.get("title", f"問題 {i+1}"),
            "instruction": prob.get("instruction", ""),
            "content": prob.get("content", ""),
            "choices": prob.get("choices", []),
            "answers": prob.get("answers", []),
            "matchType": prob.get("matchType", "exact")
        }

        if chapter_title in chapter_map:
            chapter_map[chapter_title]["lessons"].append(lesson)
        else:
            new_ch = {"title": chapter_title, "lessons": [lesson]}
            chapters.append(new_ch)
            chapter_map[chapter_title] = new_ch

    return existing_data


def rebuild_catalog():
    """update_catalog.py を実行して通し番号・カタログを再構築する"""
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "update_catalog.py")
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            cwd=os.path.dirname(script_path),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if result.returncode == 0:
            print("[OK] update_catalog.py を実行し、カタログを再構築しました。")
        else:
            print("[WARN] update_catalog.py の実行に失敗しました。")
            if result.stderr:
                print(result.stderr)
    except Exception as e:
        print(f"[WARN] カタログ再構築で例外が発生しました: {e}")


# ============================================================
# メイン処理
# ============================================================

def generate_for_path(path: str, count: int, use_reference: bool = False, engine: str = "ollama"):
    """指定パスに対して問題を生成しデータに保存する"""
    print(f"\n{'='*60}")
    print(f"[生成開始] パス: {path}")
    print(f"[生成開始] 目標数: {count}問")
    print(f"[生成開始] エンジン: {engine}")

    template, topic, level = get_prompt_info(path)
    print(f"[生成開始] トピック: {topic}")
    print(f"[生成開始] レベル: {level}")

    # 英語問題の場合は GrammarSelector で文法事項を抽選する
    selector = GrammarSelector() if "english" in path else None
    selected_items: list = []

    success_count = 0
    for i in range(count):
        print(f"  [{i+1}/{count}] 生成中...", end="", flush=True)
        start_time = time.time()

        # プロンプトを構築（英語は文法事項を抽選して埋め込む）
        if selector is not None:
            n = GrammarSelector.get_count_for_level(path)
            selected_items = selector.select_items(n)
            selected_grammar_str = "\n".join(f"- {item}" for item in selected_items)
            print(f"\n    [文法抽選] {', '.join(selected_items)}")
            print(f"  [{i+1}/{count}] 生成中...", end="", flush=True)
            prompt = template.format(count=1, topic=topic, level=level, selected_grammar=selected_grammar_str)
        else:
            selected_items = []
            prompt = template.format(count=1, topic=topic, level=level)
        
        # 同一ラン内での重複を避けるため、毎回最新の既存データを読み込んで参照に含める
        if use_reference:
            existing_data = load_problems_for_path(path)
            existing_lessons = []
            if "chapters" in existing_data:
                for ch in existing_data["chapters"]:
                    if "lessons" in ch:
                        for lesson in ch["lessons"]:
                            title = lesson.get('title', '')
                            instruction = lesson.get('instruction', '').replace('\n', ' ')
                            existing_lessons.append(f"- {title}: {instruction}")
            
            if existing_lessons:
                # 文字数制限を考慮し、直近の30件程度に絞る（必要なら）
                ref_list = existing_lessons[-30:]
                prompt += "\n\n【既存の問題（これらと内容や数値が重複しないように作成してください）】\n"
                prompt += "\n".join(ref_list)

        try:
            response = call_llm(prompt, engine=engine)
            problems = parse_llm_response(response)
            
            if problems:
                # 1問ずつ即座に保存
                existing_data = load_problems_for_path(path)
                merged_data = merge_problems(existing_data, path, [problems[0]]) # 最初の1問を使用
                save_problems_data(path, merged_data)
                
                elapsed = time.time() - start_time
                print(f"\r  [{i+1}/{count} 完了] ({elapsed:.1f}秒) - {problems[0].get('title', '無題')}")
                success_count += 1
                # 使用した文法事項を履歴に記録
                if selector is not None and selected_items:
                    selector.record_usage(selected_items)
                # Gemini の場合は RPM 制限 (15回/分) 回避のため待機を入れる
                if engine == "gemini":
                    time.sleep(1)
            else:
                print(f"\r  [{i+1}/{count} 失敗] 生成結果が空でした。")
        except Exception as e:
            print(f"\r  [{i+1}/{count} エラー] {e}")

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now_str}] [完了] {path}: {success_count}/{count} 問の生成に成功しました。")
    if success_count > 0:
        rebuild_catalog()


def get_all_leaf_paths():
    """index.htmlのrootDataから空のleafディレクトリのパスを列挙する"""
    paths = []
    levels = ["level_A", "level_B", "level_C", "level_D"]

    # English
    for cat in ["short_fill", "long_reading", "translation_ej", "translation_je"]:
        for level in ["level_A", "level_B", "level_C", "level_D"]:
            paths.append(f"english/{cat}/{level}")

    # 数学1
    math1_units = [
        "numbers_and_expressions/calculation",
        "numbers_and_expressions/real_numbers",
        "numbers_and_expressions/inequalities",
        "logic_and_sets/sets",
        "logic_and_sets/logic",
        "quadratics/graph",
        "quadratics/equations_inequalities",
        "trigonometry/acute",
        "trigonometry/extension",
        "trigonometry/application",
        "data_analysis/variance",
        "data_analysis/correlation",
        "data_analysis/application",
    ]
    for unit in math1_units:
        for level in levels:
            paths.append(f"math/math_1/{unit}/{level}")

    # 数学A
    math_a_units = [
        "probability/sets", "probability/counts",
        "probability/basics", "probability/various",
        "geometry/triangles", "geometry/circles", "geometry/solid",
        "human_activity/living", "human_activity/enjoying",
    ]
    for unit in math_a_units:
        for level in levels:
            paths.append(f"math/math_a/{unit}/{level}")

    # 数学II
    math2_units = [
        "equations_proof/calculation", "equations_proof/quadratics",
        "equations_proof/higher", "equations_proof/proof",
        "coordinates/lines", "coordinates/circles", "coordinates/loci",
        "trigonometry/functions", "trigonometry/addition",
        "exponential_log/exponential", "exponential_log/logarithmic",
        "calculus/differentiation", "calculus/integration",
    ]
    for unit in math2_units:
        for level in levels:
            paths.append(f"math/math_2/{unit}/{level}")

    # 数学B
    math_b_units = [
        "sequences/basics", "sequences/induction",
        "statistics/sampling", "statistics/distribution",
        "statistics/normal", "statistics/inference",
        "society/phenomena",
    ]
    for unit in math_b_units:
        for level in levels:
            paths.append(f"math/math_b/{unit}/{level}")

    # 数学III
    math3_units = [
        "functions_limits/functions", "functions_limits/sequence_limits",
        "functions_limits/function_limits",
        "differentiation/basics", "differentiation/derivatives",
        "differentiation_apps/increase_decrease", "differentiation_apps/various",
        "integration/indefinite", "integration/definite", "integration/applications",
    ]
    for unit in math3_units:
        for level in levels:
            paths.append(f"math/math_3/{unit}/{level}")

    # 数学C
    math_c_units = [
        "vectors/plane", "vectors/application", "vectors/space",
        "curves/quadrics", "curves/polar",
        "complex_plane/basics", "complex_plane/application",
        "representation/matrices", "representation/data",
    ]
    for unit in math_c_units:
        for level in levels:
            paths.append(f"math/math_c/{unit}/{level}")

    return paths


def initialize_folders():
    """すべての単元・難易度のフォルダをあらかじめ作成する"""
    print("\n[INFO] フォルダ構成を初期化しています...")
    paths = get_all_leaf_paths()
    for path in paths:
        dir_path = os.path.join(PROBLEMS_DIR, path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
    print(f"[OK] {len(paths)} 個のフォルダ構造を確認・作成しました。")


def select_path_interactively():
    """階層メニューでパスを選択する"""
    all_paths = get_all_leaf_paths()
    
    # 階層構造を構築
    tree = {}
    for p in all_paths:
        parts = p.split('/')
        if len(parts) < 3: continue
        
        subj = parts[0]
        unit = "/".join(parts[1:-1])
        level = parts[-1]
        
        if subj not in tree: tree[subj] = {}
        if unit not in tree[subj]: tree[subj][unit] = []
        if level not in tree[subj][unit]: tree[subj][unit].append(level)

    # 1. 科目選択
    subjects = sorted(list(tree.keys()))
    print("\n--- 科目を選択してください ---")
    for i, s in enumerate(subjects):
        print(f"  {i+1}: {to_display_name(s)}")
    
    s_idx = int(input(f"\n選択 (1-{len(subjects)}): ") or 1) - 1
    selected_subj = subjects[s_idx]

    # 2. 単元選択
    units = sorted(list(tree[selected_subj].keys()))
    print(f"\n--- [{to_display_name(selected_subj)}] 単元を選択してください ---")
    for i, u in enumerate(units):
        print(f"  {i+1}: {to_display_name(u)}")
    
    u_idx = int(input(f"\n選択 (1-{len(units)}): ") or 1) - 1
    selected_unit = units[u_idx]

    # 3. レベル選択
    levels = sorted(tree[selected_subj][selected_unit])
    print(f"\n--- [{to_display_name(selected_unit)}] 難易度を選択してください ---")
    for i, l in enumerate(levels):
        desc = ""
        if "level_A" in l: desc = " (教科書 基本・標準)"
        if "level_B" in l: desc = " (教科書 発展)"
        if "level_C" in l: desc = " (共通テスト)"
        if "level_D" in l: desc = " (二次試験)"
        print(f"  {i+1}: {l}{desc}")
    
    l_idx = int(input(f"\n選択 (1-{len(levels)}): ") or 1) - 1
    selected_level = levels[l_idx]

    return f"{selected_subj}/{selected_unit}/{selected_level}"


def main():
    global MODEL_NAME, OLLAMA_URL
    
    parser = argparse.ArgumentParser(description="Gemma4 E4B で演習問題を自動生成")
    parser.add_argument("--path", type=str, help="問題を生成するパス (例: math/math_1/quadratics/graph)")
    parser.add_argument("--count", type=int, help="1パスあたりの問題数")
    parser.add_argument("--batch", type=str, help="バッチ設定JSONファイル")
    parser.add_argument("--auto", action="store_true", help="全ての空パスに自動生成")
    parser.add_argument("--init", action="store_true", help="フォルダ構成のみ初期化")
    parser.add_argument("--model", type=str, default=MODEL_NAME, help=f"使用モデル名 (default: {MODEL_NAME})")
    parser.add_argument("--url", type=str, default=OLLAMA_URL, help=f"Ollama API URL (default: {OLLAMA_URL})")
    parser.add_argument("--engine", type=str, choices=["ollama", "gemini"], default="ollama", help="使用するAIエンジン (default: ollama)")
    args = parser.parse_args()

    MODEL_NAME = args.model
    OLLAMA_URL = args.url

    if args.init:
        initialize_folders()
        sys.exit(0)

    # 対話モードの判定
    is_interactive = not (args.path or args.batch or args.auto)
    
    print("=" * 60)
    print("  CodeJourney 問題自動生成ツール")
    print(f"  モデル: {MODEL_NAME}")
    print(f"  API: {OLLAMA_URL}")
    print("=" * 60)

    # 既存データ読み込み
    available_paths = get_available_paths()
    print(f"[INFO] 既存データ: {len(available_paths)}パス分のデータを読み込みました。")

    paths_to_generate = []
    default_count = args.count or 5

    use_reference = False

    if is_interactive:
        while True:
            print("\n生成モードを選択してください:")
            print("  1: 単元をメニューから選んで生成")
            print("  2: 問題がない全ての空単元に自動生成")
            print("  3: 設定ファイル(batch_config.json)から一括生成")
            print("  f: フォルダ構成をすべて事前に作成")
            print(f"  s: 設定変更 (現在: {MODEL_NAME})")
            print("  q: 終了")
            
            choice = input("\n選択 (1/2/3/f/s/q): ").strip().lower()
            if choice == 'q':
                sys.exit(0)
            
            if choice == 'f':
                initialize_folders()
                continue
            
            if choice == 's':
                new_model = input(f"使用するモデル名を入力してください (現在: {MODEL_NAME}): ").strip()
                if new_model: MODEL_NAME = new_model
                new_url = input(f"OllamaのURLを入力してください (現在: {OLLAMA_URL}): ").strip()
                if new_url: OLLAMA_URL = new_url
                print(f"[OK] 設定を更新しました。")
                continue

            if choice == '1':
                try:
                    path = select_path_interactively()
                    paths_to_generate = [path]
                    
                    cnt_str = input(f"\n生成する問題数を入力してください (デフォルト: {default_count}): ").strip()
                    if cnt_str: default_count = int(cnt_str)
                    
                    ref_choice = input("既存の問題を素材として読み込み、問題の丸パクリ（重複）を避けますか？ (y/n) [デフォルト: y]: ").strip().lower()
                    use_reference = ref_choice != 'n'
                    break
                except (ValueError, IndexError):
                    print("[ERROR] 正しい番号を入力してください。")
                    continue
                
            elif choice == '2':
                all_paths = get_all_leaf_paths()
                paths_to_generate = [p for p in all_paths if p not in available_paths]
                print(f"[INFO] 未生成の単元が {len(paths_to_generate)} 件見つかりました。")
                cnt_str = input(f"各単元ごとに生成する問題数を入力してください (デフォルト: 3): ").strip()
                default_count = int(cnt_str) if cnt_str else 3
                
                ref_choice = input("既存の問題を素材として読み込み、問題の丸パクリ（重複）を避けますか？ (y/n) [デフォルト: y]: ").strip().lower()
                use_reference = ref_choice != 'n'
                break
                
            elif choice == '3':
                batch_file = input("設定ファイル名を入力してください (デフォルト: batch_config.json): ").strip() or "batch_config.json"
                if not os.path.exists(batch_file):
                    print(f"[ERROR] ファイルが見つかりません: {batch_file}")
                    continue
                args.batch = batch_file
                with open(args.batch, "r", encoding="utf-8") as f:
                    batch_config = json.load(f)
                paths_to_generate = [item["path"] for item in batch_config]
                
                ref_choice = input("既存の問題を素材として読み込み、問題の丸パクリ（重複）を避けますか？ (y/n) [デフォルト: y]: ").strip().lower()
                use_reference = ref_choice != 'n'
                break
            else:
                print("[ERROR] 不正な選択です。")
    else:
        # 引数指定モード
        if args.path:
            paths_to_generate = [args.path]
        elif args.batch:
            with open(args.batch, "r", encoding="utf-8") as f:
                batch_config = json.load(f)
            paths_to_generate = [item["path"] for item in batch_config]
        elif args.auto:
            all_paths = get_all_leaf_paths()
            paths_to_generate = [p for p in all_paths if p not in available_paths]
            print(f"[INFO] 自動モード: {len(paths_to_generate)}/{len(all_paths)}パスが未生成です。")

    if not paths_to_generate:
        print("[INFO] 生成対象のパスがありません。")
        sys.exit(0)

    total = len(paths_to_generate)
    success = 0
    failed = 0

    print(f"\n合計 {total} パスの処理を開始します。")
    
    # 引数で指定がない場合はエンジンを選択させる
    selected_engine = args.engine
    if not (args.path or args.batch or args.auto):
        print("\n使用するエンジンを選択してください:")
        print("1. Ollama (ローカル / 無料)")
        print("2. Gemini (API / 高精度)")
        eng_choice = input("選択 (1/2): ").strip()
        selected_engine = "gemini" if eng_choice == "2" else "ollama"

    for i, path in enumerate(paths_to_generate):
        print(f"\n[{i+1}/{total}] 処理中...")
        try:
            count = default_count
            # バッチモードの場合、個別のcount設定があれば優先
            if args.batch:
                with open(args.batch, "r", encoding="utf-8") as f:
                    batch_config = json.load(f)
                for item in batch_config:
                    if item["path"] == path:
                        count = item.get("count", default_count)
                        break

            generate_for_path(path, count, use_reference, engine=selected_engine)
            success += 1

        except Exception as e:
            print(f"[ERROR] {path}: {e}")
            failed += 1
            continue

    print(f"\n{'='*60}")
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now_str}] [完了] 成功: {success}, 失敗: {failed}, 合計: {total}")
    print(f"[{now_str}] [完了] problems/ フォルダ以下に保存しました。")
    print(f"[{now_str}] [完了] ブラウザでindex.htmlをリロードすると反映されます。")


if __name__ == "__main__":
    main()
