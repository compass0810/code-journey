import os
import json
import re

PROBLEMS_DIR = "problems"
CATALOG_FILE = os.path.join(PROBLEMS_DIR, "catalog.js")
CATALOG_JSON_FILE = os.path.join(PROBLEMS_DIR, "catalog.json")


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


def difficulty_to_level(difficulty: float) -> str:
    """難易度定数からレベル文字（A/B/C/D）を返す"""
    if difficulty < 4.0:
        return "A"
    if difficulty < 7.0:
        return "B"
    if difficulty < 9.0:
        return "C"
    return "D"

# パスから科目を判定するためのマッピング
SUBJECT_MAP = {
    "math/math_1": "数学I",
    "math/math_a": "数学A",
    "math/math_2": "数学II",
    "math/math_b": "数学B",
    "math/math_3": "数学III",
    "math/math_c": "数学C",
    "english/short_fill": "英語（短文補充）",
    "english/long_reading": "英語（長文読解）",
    "english/translation_ej": "英語（英文和訳）",
    "english/translation_je": "英語（和文英訳）",
}

def get_subject_info(path):
    # パスが SUBJECT_MAP のキーで始まるかチェック
    for prefix, name in SUBJECT_MAP.items():
        if path.startswith(prefix):
            return prefix, name
    return None, None

def update_data_js(file_path, subject_name, counters, rel_path=""):
    """data.js を読み込み、chapters/lessons 内の各問題に番号・difficulty を付与する（無い場合のみ）"""
    if not os.path.exists(file_path):
        return 0

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # JSON 部分を抽出
    match = re.search(r"window\.practiceData\[\".*\"\] = (\{.*\});", content, re.DOTALL)
    if not match:
        return 0

    try:
        data = json.loads(match.group(1))
        lessons_count = 0
        modified = False
        default_difficulty = get_default_difficulty(rel_path)
        
        if "chapters" in data:
            for chapter in data["chapters"]:
                if "lessons" in chapter:
                    for lesson in chapter["lessons"]:
                        sn = lesson.get("serial_number", "")
                        has_valid_sn = sn.startswith(subject_name) and re.search(r"No\.(\d+)", sn)
                        
                        if not has_valid_sn:
                            counters[subject_name] += 1
                            lesson["serial_number"] = f"{subject_name} No.{counters[subject_name]}"
                            modified = True
                            
                        if "subject_display" not in lesson or lesson["subject_display"] != subject_name:
                            lesson["subject_display"] = subject_name
                            modified = True

                        # difficulty が未設定の場合はパスから自動付与
                        if "difficulty" not in lesson:
                            lesson["difficulty"] = default_difficulty
                            modified = True
                            
                        lessons_count += 1
        
        if modified:
            new_json = json.dumps(data, indent=4, ensure_ascii=False)
            new_content = content.replace(match.group(1), new_json)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            
        return lessons_count
    except Exception as e:
        print(f"  [ERROR] {file_path} のパースに失敗: {e}")
        return 0

def main():
    print("問題スキャン開始...")
    catalog = []
    
    all_dirs = []
    for root, dirs, files in os.walk(PROBLEMS_DIR):
        if "data.js" in files:
            rel_path = os.path.relpath(root, PROBLEMS_DIR).replace("\\", "/")
            all_dirs.append((rel_path, os.path.join(root, "data.js")))
            
    all_dirs.sort()

    counters = {k: 0 for k in SUBJECT_MAP.values()}
    for rel_path, file_path in all_dirs:
        prefix, subject_name = get_subject_info(rel_path)
        if not subject_name: continue
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            match = re.search(r"window\.practiceData\[\".*\"\] = (\{.*\});", content, re.DOTALL)
            if match:
                data = json.loads(match.group(1))
                for chapter in data.get("chapters", []):
                    for lesson in chapter.get("lessons", []):
                        sn = lesson.get("serial_number", "")
                        if sn.startswith(subject_name):
                            m = re.search(r"No\.(\d+)", sn)
                            if m:
                                counters[subject_name] = max(counters[subject_name], int(m.group(1)))
        except:
            pass

    for rel_path, file_path in all_dirs:
        prefix, subject_name = get_subject_info(rel_path)
        if not subject_name:
            continue
            
        count = update_data_js(file_path, subject_name, counters, rel_path)
        
        if count > 0:
            # カタログ用データを再読み込みして収集
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                match = re.search(r"window\.practiceData\[\".*\"\] = (\{.*\});", content, re.DOTALL)
                data = json.loads(match.group(1))
                
                for chapter in data.get("chapters", []):
                    for lesson in chapter.get("lessons", []):
                        difficulty = lesson.get("difficulty", get_default_difficulty(rel_path))
                        catalog.append({
                            "id": lesson.get("id", ""),
                            "serial_number": lesson["serial_number"],
                            "subject_display": lesson["subject_display"],
                            "title": lesson["title"],
                            "path": rel_path,
                            "level": rel_path.split("/")[-1],
                            "chapter_title": chapter.get("title", ""),
                            "difficulty": difficulty,
                            "difficulty_level": difficulty_to_level(difficulty)
                        })
            
            print(f"完了: {rel_path} ({count}問読込)")

    def serial_sort_key(item):
        serial_number = item.get("serial_number", "")
        match = re.search(r"No\.(\d+)", serial_number)
        number = int(match.group(1)) if match else 10**9
        return (item.get("subject_display", ""), number, item.get("path", ""), item.get("title", ""))

    catalog.sort(key=serial_sort_key)

    # catalog.js / catalog.json を両方保存
    js_content = f"window.problemCatalog = {json.dumps(catalog, indent=4, ensure_ascii=False)};"
    with open(CATALOG_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
    with open(CATALOG_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=4, ensure_ascii=False)
        
    print(f"\n[完了] {len(catalog)} 問に番号を振りました。")
    print(f"カタログファイルを保存しました: {CATALOG_FILE}")
    print(f"カタログJSONを保存しました: {CATALOG_JSON_FILE}")

if __name__ == "__main__":
    main()
