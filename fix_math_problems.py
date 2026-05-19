"""
fix_math_problems.py
数学の data.js ファイルから重複問題を削除し、serial_number を振り直すスクリプト
"""
import os, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

PROBLEMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "problems")
MATH_DIR = os.path.join(PROBLEMS_DIR, "math")

SUBJECT_DISPLAY_MAP = {
    "math_1": "数学I",
    "math_a": "数学A",
    "math_2": "数学II",
    "math_b": "数学B",
    "math_3": "数学III",
    "math_c": "数学C",
}

def parse_data_js(content: str):
    match = re.search(r'window\.practiceData\[.*?\]\s*=\s*(\{[\s\S]*?\});\s*$', content, re.MULTILINE)
    if not match:
        # Try without $ anchor
        match = re.search(r'window\.practiceData\[.*?\]\s*=\s*(\{[\s\S]*\});', content)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except:
        return None

def deduplicate_chapters(data: dict) -> dict:
    """
    章をフラットにして、同じinstructionの問題は1つだけ残す。
    全問題を1つのchapterにまとめ直す。
    """
    seen_instructions = set()
    unique_lessons = []
    
    for ch in data.get("chapters", []):
        for lesson in ch.get("lessons", []):
            instr = lesson.get("instruction", "").strip()
            if instr and instr in seen_instructions:
                continue  # 重複をスキップ
            seen_instructions.add(instr)
            unique_lessons.append(lesson)
    
    # 全問題を1つのchapterに統合
    if not unique_lessons:
        return data
    
    # 元データのchapterタイトルを取得 (最初の正式なタイトルを使う)
    chapter_title = "演習問題"
    for ch in data.get("chapters", []):
        title = ch.get("title", "")
        # 英語のpath名でないもの (日本語) を優先
        if title and not re.match(r'^[a-z_/]+$', title):
            chapter_title = title
            break
    if chapter_title == "演習問題":
        # 最初のchapterのタイトルを使う
        if data.get("chapters"):
            chapter_title = data["chapters"][0].get("title", "演習問題")
    
    return {"chapters": [{"title": chapter_title, "lessons": unique_lessons}]}

def reassign_serial_numbers(all_file_data: list, subj_key: str, subject_display: str):
    """
    subj_key (例: math_1) に属する全ファイルの問題を通し番号で振り直す。
    all_file_data: [{file_path, path_key, data}, ...]
    """
    # 全問題を収集
    all_lessons = []
    for entry in all_file_data:
        for ch in entry['data'].get('chapters', []):
            for lesson in ch.get('lessons', []):
                all_lessons.append((entry, lesson))
    
    # 通し番号を振り直す
    for i, (entry, lesson) in enumerate(all_lessons, start=1):
        lesson['serial_number'] = f"{subject_display} No.{i}"
        lesson['subject_display'] = subject_display
    
    print(f"  {subject_display}: {len(all_lessons)} 問に通し番号を割り当て")
    return len(all_lessons)

def save_data_js(file_path: str, path_key: str, data: dict):
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    content = f"""// Auto-generated problem data
window.practiceData = window.practiceData || {{}};
window.practiceData["{path_key}"] = {json_str};
"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("=== 数学問題データの修正を開始 ===\n")
    
    total_removed = 0
    
    for subj_key, subject_display in SUBJECT_DISPLAY_MAP.items():
        subj_dir = os.path.join(MATH_DIR, subj_key)
        if not os.path.exists(subj_dir):
            continue
        
        print(f"\n--- {subject_display} ({subj_key}) の処理 ---")
        
        # 全data.jsを読み込む
        all_file_data = []
        for root, dirs, files in os.walk(subj_dir):
            if 'data.js' not in files:
                continue
            file_path = os.path.join(root, 'data.js')
            rel = os.path.relpath(root, PROBLEMS_DIR).replace(os.sep, '/')
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            data = parse_data_js(content)
            if not data:
                print(f"  [WARN] パースできませんでした: {rel}")
                continue
            
            # 重複除去前の問題数
            before_count = sum(len(ch.get('lessons', [])) for ch in data.get('chapters', []))
            
            # 重複除去
            data = deduplicate_chapters(data)
            
            # 重複除去後の問題数
            after_count = sum(len(ch.get('lessons', [])) for ch in data.get('chapters', []))
            removed = before_count - after_count
            if removed > 0:
                print(f"  {rel}: {before_count}問 → {after_count}問 ({removed}問削除)")
                total_removed += removed
            
            all_file_data.append({
                'file_path': file_path,
                'path_key': rel,
                'data': data,
            })
        
        # 通し番号を振り直す
        reassign_serial_numbers(all_file_data, subj_key, subject_display)
        
        # ファイルに保存
        for entry in all_file_data:
            save_data_js(entry['file_path'], entry['path_key'], entry['data'])
        
        print(f"  ✓ {len(all_file_data)} ファイルを保存しました")
    
    print(f"\n=== 完了: 合計 {total_removed} 問の重複を削除しました ===")
    
    # catalog を再構築
    print("\n--- カタログを再構築します ---")
    import subprocess
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "update_catalog.py")
    result = subprocess.run(
        [sys.executable, script_path],
        cwd=os.path.dirname(script_path),
        capture_output=True, text=True, encoding='utf-8', errors='replace'
    )
    if result.returncode == 0:
        print("[OK] カタログを再構築しました")
        print(result.stdout[-500:] if result.stdout else "")
    else:
        print("[ERROR] カタログ再構築に失敗しました")
        print(result.stderr[-500:] if result.stderr else "")

if __name__ == "__main__":
    main()
