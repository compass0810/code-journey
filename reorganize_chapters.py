import os
import json
import re

# ============================================================
# 設定
# ============================================================
PROBLEMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "problems", "english")

# ============================================================
# マッピングルール
# ============================================================

GRAMMAR_MAP = {
    "文法：時制": [
        "時制", "現在形", "過去形", "未来形", "進行形", "完了形", "現在完了", "過去完了", "未来完了", "時制の一致"
    ],
    "文法：助動詞": [
        "助動詞", "can", "may", "must", "should", "will", "would", "shall", "ought to"
    ],
    "文法：不定詞・動名詞": [
        "不定詞", "動名詞", "to不定詞", "原形不定詞", "infinitive", "gerund", "It...to"
    ],
    "文法：分詞・分詞構文": [
        "分詞", "現在分詞", "過去分詞", "分詞構文", "participle"
    ],
    "文法：受動態": [
        "受動態", "受身", "passive"
    ],
    "文法：比較": [
        "比較", "比較級", "最上級", "comparison", "comparative", "superlative", "as as"
    ],
    "文法：関係詞": [
        "関係詞", "関係代名詞", "関係副詞", "複合関係", "relative"
    ],
    "文法：仮定法": [
        "仮定法", "subjunctive", "If I were"
    ],
    "文法：接続詞": [
        "接続詞", "conjunction", "because", "although", "unless", "since"
    ],
    "文法：前置詞": [
        "前置詞", "preposition", "at", "in", "on", "with", "by", "for"
    ],
    "文法：代名詞・冠詞": [
        "代名詞", "冠詞", "pronoun", "article", "a", "an", "the"
    ],
    "文法：否定・倒置・強調": [
        "否定", "倒置", "強調", "negative", "inversion", "emphasis", "emphatic"
    ],
    "語彙・熟語・表現": [
        "語彙", "熟語", "表現", "vocabulary", "idiom", "expression", "コロケーション", "慣用", "単語", "形容詞", "副詞", "名詞"
    ]
}

THEME_MAP = {
    "テーマ：科学・技術": [
        "科学", "技術", "テクノロジー", "AI", "人工知能", "宇宙", "医学", "科学的", "コンピュータ", "発明", "エネルギー", "研究"
    ],
    "テーマ：社会・経済・政治": [
        "社会", "経済", "政治", "法律", "国際", "歴史", "平和", "労働", "人口", "都市", "貧困", "グローバル"
    ],
    "テーマ：文化・歴史・芸術": [
        "文化", "歴史", "芸術", "伝統", "習慣", "言語", "文学", "宗教", "音楽", "映画", "観光"
    ],
    "テーマ：自然・環境": [
        "自然", "環境", "地球", "気候", "温暖化", "動物", "植物", "生態系", "海洋", "災害", "サステナブル", "再生可能"
    ],
    "テーマ：日常生活・教育・心理": [
        "日常", "教育", "心理", "健康", "スポーツ", "学校", "家族", "友人", "コミュニケーション", "自己啓発", "旅行", "趣味"
    ],
    "テーマ：ビジネス": [
        "ビジネス", "仕事", "マーケティング", "会社", "経営", "会議", "プレゼン", "契約"
    ]
}

def get_new_category(original_title, lesson_title, is_grammar_priority=True):
    # 文法優先かテーマ優先か（short_fillは文法、それ以外はテーマ）
    maps_to_check = []
    if is_grammar_priority:
        maps_to_check = [GRAMMAR_MAP, THEME_MAP]
    else:
        maps_to_check = [THEME_MAP, GRAMMAR_MAP]

    text_to_check = (original_title + " " + lesson_title).lower()
    
    for category_map in maps_to_check:
        for cat_name, keywords in category_map.items():
            for kw in keywords:
                if kw.lower() in text_to_check:
                    return cat_name
    
    return "その他"

# ============================================================
# メインロジック
# ============================================================

def process_file(file_path, rel_path):
    print(f"Processing: {rel_path}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # window.practiceData[...] = { ... } の抽出
    match = re.search(r'window\.practiceData\["?[^"]+"?\]\s*=\s*(\{[\s\S]*\});?\s*$', content)
    if not match:
        print(f"  [SKIP] Could not parse JSON from {rel_path}")
        return

    js_obj_str = match.group(1)
    try:
        data = json.loads(js_obj_str)
    except Exception as e:
        print(f"  [ERROR] JSON load failed: {e}")
        return

    if "chapters" not in data:
        print(f"  [SKIP] No chapters in {rel_path}")
        return

    # 全レッスンを抽出
    all_lessons = []
    for ch in data["chapters"]:
        ch_title = ch.get("title", "")
        for lesson in ch.get("lessons", []):
            lesson["_original_chapter"] = ch_title
            all_lessons.append(lesson)

    if not all_lessons:
        return

    # 分類
    is_short_fill = "short_fill" in rel_path
    organized = {}
    
    for lesson in all_lessons:
        orig_ch = lesson.pop("_original_chapter", "")
        cat = get_new_category(orig_ch, lesson.get("title", ""), is_grammar_priority=is_short_fill)
        
        if cat not in organized:
            organized[cat] = []
        organized[cat].append(lesson)

    # チャプター再構成
    # ソート順を定義（文法→テーマ→その他）
    all_cat_names = list(GRAMMAR_MAP.keys()) + list(THEME_MAP.keys()) + ["その他"]
    
    new_chapters = []
    for cat_name in all_cat_names:
        if cat_name in organized:
            new_chapters.append({
                "title": cat_name,
                "lessons": organized[cat_name]
            })

    data["chapters"] = new_chapters

    # 保存
    new_json_str = json.dumps(data, ensure_ascii=False, indent=4)
    path_key = rel_path.replace("\\", "/").replace(".js", "")
    if path_key.endswith("/data"):
        path_key = path_key[:-5]

    new_content = f"""// Auto-organized problem data
window.practiceData = window.practiceData || {{}};
window.practiceData["{path_key}"] = {new_json_str};
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  [SUCCESS] Organized into {len(new_chapters)} chapters.")

def main():
    for root, dirs, files in os.walk(PROBLEMS_DIR):
        for file in files:
            if file == "data.js":
                full_path = os.path.join(root, file)
                # problems ディレクトリからの相対パス
                rel_path = os.path.relpath(full_path, os.path.dirname(PROBLEMS_DIR))
                process_file(full_path, rel_path)

if __name__ == "__main__":
    main()
