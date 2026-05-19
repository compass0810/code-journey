"""
update_difficulty_with_ai.py - Gemini API を使用して全問題の難易度を再評価するスクリプト

100問単位のバッチ処理を行い、問題の内容に基づいた 1.0〜11.0 の詳細な難易度を付与する。
"""

import os
import json
import re
import time
import sys
import subprocess
import google.generativeai as genai

# 設定
GEMINI_API_KEY = "AIzaSyDWECPPrJ3tXKxxJ0AMFKPyBadBzTVJl04"
GEMINI_MODEL_NAME = "gemini-3.1-flash-lite"
PROBLEMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "problems")

# 教科表示名
SUBJECT_DISPLAY_MAP = {
    "math/math_1": "数学I", "math/math_a": "数学A", "math/math_2": "数学II",
    "math/math_b": "数学B", "math/math_3": "数学III", "math/math_c": "数学C",
    "english/short_fill": "英語（短文補充）", "english/long_reading": "英語（長文読解）",
    "english/translation_ej": "英語（英文和訳）", "english/translation_je": "英語（和文英訳）"
}

def setup_gemini():
    if not GEMINI_API_KEY:
        print("[ERROR] Gemini API Key が設定されていません。")
        sys.exit(1)
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel(GEMINI_MODEL_NAME)

def get_difficulty_from_ai(model, problems_batch):
    """
    AIに問題リストを送り、それぞれの難易度定数（1.0-11.0）を返させる。
    """
    prompt = f"""
あなたは教育専門家として、プログラミング学習プラットフォームにおける問題の難易度を評価してください。
以下の問題リスト（JSON）を分析し、各問題に対して 1.0 から 11.0 の範囲で難易度定数を 0.1 刻みで決定してください。

【評価基準】
- 1.0 〜 3.9 (レベルA): 教科書基本〜標準。基礎知識の確認。
- 4.0 〜 6.9 (レベルB): 教科書発展〜入試基礎。典型的な解法の適用。
- 7.0 〜 8.9 (レベルC): 共通テスト〜中堅私大レベル。思考力や応用力が必要。
- 9.0 〜 11.0 (レベルD): 難関大・二次試験レベル。高度な発想や複雑な論理展開。

※与えられた `current_level` (A/B/C/D) は強力なガイドラインですが、内容がそれより難しい、あるいは易しいと感じる場合は適切な数値を優先してください。

【出力形式】
JSON形式のみで出力してください。他の説明は不要です。
[
  {{"id": "問題ID", "difficulty": 2.4}},
  ...
]

【問題リスト】
{json.dumps(problems_batch, ensure_ascii=False, indent=2)}
"""
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        # JSON部分を抽出
        match = re.search(r'\[\s*\{.*\}\s*\]', text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        else:
            print(f"  [WARN] AIの応答からJSONを抽出できませんでした。テキスト: {text[:200]}...")
            return None
    except Exception as e:
        print(f"  [ERROR] Gemini API 呼び出しエラー: {e}")
        return None

def process_batch(model, batch_data):
    """
    batch_data: list of (rel_path, file_path, lesson_obj)
    """
    ai_input = []
    for rel_path, file_path, lesson in batch_data:
        ai_input.append({
            "id": lesson["id"],
            "title": lesson.get("title", ""),
            "content": lesson.get("content", "")[:300], # 長すぎる場合はカット
            "current_level": rel_path.split("/")[-1].replace("level_", "")
        })

    results = get_difficulty_from_ai(model, ai_input)
    if not results:
        return 0

    # 結果をマッピング
    id_to_diff = {r["id"]: r["difficulty"] for r in results if "id" in r and "difficulty" in r}
    
    # 各ファイルを更新
    updated_files = set()
    files_to_lessons = {}
    for rel_path, file_path, lesson in batch_data:
        if file_path not in files_to_lessons:
            files_to_lessons[file_path] = []
        files_to_lessons[file_path].append(lesson)

    updated_count = 0
    for file_path, lessons in files_to_lessons.items():
        # ファイルを読み込み、対象のIDの難易度を更新
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        match = re.search(r'window\.practiceData\["?(.*?)"?\]\s*=\s*(\{[\s\S]*?\});?\s*$', content)
        if not match: continue
        key = match.group(1)
        data = json.loads(match.group(2))
        
        modified = False
        for chapter in data.get("chapters", []):
            for lesson in chapter.get("lessons", []):
                if lesson["id"] in id_to_diff:
                    lesson["difficulty"] = float(id_to_diff[lesson["id"]])
                    updated_count += 1
                    modified = True
        
        if modified:
            new_json = json.dumps(data, ensure_ascii=False, indent=4)
            new_content = f'window.practiceData = window.practiceData || {{}};\nwindow.practiceData["{key}"] = {new_json};'
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
    
    return updated_count

def main():
    model = setup_gemini()
    print("=" * 60)
    print("  AIによる難易度再評価スクリプト")
    print("=" * 60)

    print("[INFO] 問題データを収集中...")
    # 全問題を収集
    all_lessons = []
    for root, dirs, files in os.walk(PROBLEMS_DIR):
        if "data.js" in files:
            rel_path = os.path.relpath(root, PROBLEMS_DIR).replace("\\", "/")
            file_path = os.path.join(root, "data.js")
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                match = re.search(r'window\.practiceData\[".*?"\]\s*=\s*(\{[\s\S]*?\});?\s*$', content)
                if not match: continue
                data = json.loads(match.group(1))
                for chapter in data.get("chapters", []):
                    for lesson in chapter.get("lessons", []):
                        all_lessons.append((rel_path, file_path, lesson))
            except Exception as e:
                print(f"  [ERROR] ファイル読み込み失敗 ({file_path}): {e}")

    total = len(all_lessons)
    print(f"[INFO] 合計 {total} 問が見つかりました。")
    
    # ユーザーが一度に全件やりたいか、テストしたいかを確認する代わりに、
    # ここでは100問ずつバッチ処理を進める
    BATCH_SIZE = 100
    total_updated = 0
    
    for i in range(0, total, BATCH_SIZE):
        batch = all_lessons[i : i + BATCH_SIZE]
        print(f"\n[バッチ {i//BATCH_SIZE + 1} / { (total+BATCH_SIZE-1)//BATCH_SIZE }] {len(batch)}問を処理中...")
        
        updated = process_batch(model, batch)
        total_updated += updated
        print(f"  -> {updated} 問の難易度を更新完了")
        
        # API制限を考慮して少し待つ
        if i + BATCH_SIZE < total:
            time.sleep(2)

    print(f"\n[完了] 合計 {total_updated} 問の難易度をAIで再評価しました。")
    
    # カタログ再構築
    subprocess.run([sys.executable, "update_catalog.py"])

if __name__ == "__main__":
    main()
