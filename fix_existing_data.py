import os
import json
import re
import uuid
import sys

PROBLEMS_DIR = "problems"
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

target_subject = None
keep_ids = False

def get_subject_info(path):
    for prefix, name in SUBJECT_MAP.items():
        if path.startswith(prefix):
            return prefix, name
    return None, None

def parse_data_js_content(content: str):
    match = re.search(r'window\.practiceData\["?[^"]+"?\]\s*=\s*(\{[\s\S]*\});?\s*$', content)
    if not match:
        return None
    return match.group(1)

def main():
    print("既存問題データの修正を開始します...")
    
    all_dirs = []
    for root, dirs, files in os.walk(PROBLEMS_DIR):
        if "data.js" in files:
            rel_path = os.path.relpath(root, PROBLEMS_DIR).replace("\\", "/")
            all_dirs.append((rel_path, os.path.join(root, "data.js")))
            
    all_dirs.sort()

    counters = {k: 0 for k in SUBJECT_MAP.values()}
    total_modified = 0

    for rel_path, file_path in all_dirs:
        prefix, subject_name = get_subject_info(rel_path)
        if not subject_name:
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        json_str = parse_data_js_content(content)
        if not json_str:
            continue

        try:
            data = json.loads(json_str)
            modified = False
            
            if "chapters" in data:
                for chapter in data["chapters"]:
                    if "lessons" in chapter:
                        for lesson in chapter["lessons"]:
                            # UUIDの再生成
                            path_prefix = rel_path.replace("/", "-")
                            lesson["id"] = f"{path_prefix}-{str(uuid.uuid4())}"
                            
                            # 通し番号の再生成
                            counters[subject_name] += 1
                            lesson["serial_number"] = f"{subject_name} No.{counters[subject_name]}"
                            lesson["subject_display"] = subject_name
                            
                            modified = True
                            total_modified += 1
                            
            if modified:
                new_json = json.dumps(data, indent=4, ensure_ascii=False)
                new_content = content.replace(json_str, new_json)
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"[更新完了] {rel_path}")

        except Exception as e:
            print(f"[エラー] {file_path} の処理に失敗: {e}")

    print(f"\n合計 {total_modified} 件の問題データを新ルール（フルUUID＆一意な通し番号）に更新しました。")
    print("カタログを再構築します...")
    
    # update_catalog.pyを呼び出してカタログを再構築する
    import update_catalog
    update_catalog.main()
    print("すべての作業が完了しました。")

if __name__ == "__main__":
    main()
