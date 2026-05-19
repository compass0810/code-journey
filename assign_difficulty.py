"""
assign_difficulty.py - 全問題に難易度定数（1.0〜11.0）を付与するバッチスクリプト

難易度定数はパスの level_X から決定論的に割り当てるため、APIリクエストは不要。

定数範囲とレベル分類:
  1.0〜3.9 → A（基本・標準）
  4.0〜6.9 → B（発展）
  7.0〜8.9 → C（共通テスト）
  9.0〜11.0 → D（二次試験）

level_A パス → difficulty 2.0
level_B パス → difficulty 5.0
level_C パス → difficulty 7.5
level_D パス → difficulty 10.0
"""

import os
import json
import re
import subprocess
import sys

PROBLEMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "problems")


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


def process_data_js(file_path: str, rel_path: str) -> tuple[int, int]:
    """
    data.js を読み込み、difficulty が未設定の問題に定数を付与して保存する。
    Returns: (total_lessons, updated_count)
    """
    if not os.path.exists(file_path):
        return 0, 0

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r"(window\.practiceData\[\".*?\"\]\s*=\s*)(\{[\s\S]*?\});\s*$", content)
    if not match:
        print(f"  [SKIP] パース失敗: {file_path}")
        return 0, 0

    prefix = match.group(1)
    json_str = match.group(2)

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"  [ERROR] JSONパースエラー ({file_path}): {e}")
        return 0, 0

    total = 0
    updated = 0
    modified = False
    default_difficulty = get_default_difficulty(rel_path)

    for chapter in data.get("chapters", []):
        for lesson in chapter.get("lessons", []):
            total += 1
            if "difficulty" not in lesson:
                lesson["difficulty"] = default_difficulty
                updated += 1
                modified = True

    if modified:
        new_json = json.dumps(data, ensure_ascii=False, indent=4)
        # 元のヘッダー（window.practiceData[...] = ...;）を復元
        header_match = re.search(r"(// Auto-generated.*?\n)", content)
        header = header_match.group(1) if header_match else ""
        
        # window.practiceData[...] = の形を維持して書き出し
        key_match = re.search(r'window\.practiceData\["([^"]+)"\]', content)
        if key_match:
            key = key_match.group(1)
            new_content = f"""// Auto-generated problem data
window.practiceData = window.practiceData || {{}};
window.practiceData["{key}"] = {new_json};
"""
        else:
            new_content = content.replace(json_str, new_json)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    return total, updated


def rebuild_catalog():
    """update_catalog.py を実行してカタログを再構築する"""
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "update_catalog.py")
    print("\n[INFO] カタログを再構築中...")
    result = subprocess.run(
        [sys.executable, script_path],
        cwd=os.path.dirname(script_path),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode == 0:
        print("[OK] カタログ再構築完了")
    else:
        print("[WARN] カタログ再構築に失敗しました")
        if result.stderr:
            print(result.stderr[:500])


def main():
    print("=" * 60)
    print("  難易度定数付与スクリプト")
    print("  ※ パスベースで決定論的に設定（APIリクエストなし）")
    print("=" * 60)

    all_files = []
    for root, dirs, files in os.walk(PROBLEMS_DIR):
        if "data.js" in files:
            rel_path = os.path.relpath(root, PROBLEMS_DIR).replace("\\", "/")
            file_path = os.path.join(root, "data.js")
            all_files.append((rel_path, file_path))

    all_files.sort()
    total_lessons = 0
    total_updated = 0

    print(f"\n[INFO] {len(all_files)} 個の data.js ファイルを処理します...\n")

    BATCH_SIZE = 100
    batch_num = 0
    for i, (rel_path, file_path) in enumerate(all_files):
        if i % BATCH_SIZE == 0:
            batch_num += 1
            print(f"--- バッチ {batch_num} (問題 {i+1}〜{min(i+BATCH_SIZE, len(all_files))}) ---")

        t, u = process_data_js(file_path, rel_path)
        total_lessons += t
        total_updated += u
        if u > 0:
            print(f"  [更新] {rel_path}: {t}問中 {u}問に定数付与")

    print(f"\n{'='*60}")
    print(f"[完了] 合計 {total_lessons} 問を処理、{total_updated} 問を更新しました。")
    print(f"  level_A → difficulty=2.0 (レベルA)")
    print(f"  level_B → difficulty=5.0 (レベルB)")
    print(f"  level_C → difficulty=7.5 (レベルC)")
    print(f"  level_D → difficulty=10.0 (レベルD)")

    rebuild_catalog()


if __name__ == "__main__":
    main()
