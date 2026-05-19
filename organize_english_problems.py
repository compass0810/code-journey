import os
import json
import re
import requests
import time
import argparse
from datetime import datetime

# ============================================================
# 設定
# ============================================================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:14b"
PROBLEMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "problems")

# ============================================================
# LLM 呼び出しロジック
# ============================================================

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
                        "temperature": 0.3, # 分類なので低めに設定
                        "num_predict": 4096,
                    }
                },
                timeout=300
            )
            resp.raise_for_status()
            return resp.json()["response"]
        except Exception as e:
            print(f"[ERROR] API呼び出しエラー (attempt {attempt+1}): {e}")
            if attempt < max_retries - 1:
                time.sleep(3)
            else:
                raise

def parse_llm_response(response_text: str) -> dict:
    """LLMのレスポンスからJSONを抽出する"""
    code_match = re.search(r"```(?:json)?\s*\n?([\s\S]*?)\n?```", response_text)
    if code_match:
        json_str = code_match.group(1).strip()
    else:
        arr_match = re.search(r"\{[\s\S]*\}", response_text)
        if arr_match:
            json_str = arr_match.group(0)
        else:
            return {}

    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return {}

# ============================================================
# ファイル操作ロジック
# ============================================================

def load_problems_for_path(path: str):
    """指定パスのデータを読み込む"""
    file_path = os.path.join(PROBLEMS_DIR, path, "data.js")
    if not os.path.exists(file_path):
        file_path = os.path.join(PROBLEMS_DIR, f"{path}.js")
        
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r'window\.practiceData\["?[^"]+"?\]\s*=\s*(\{[\s\S]*\});?\s*$', content)
    if not match:
        return None

    js_obj = match.group(1)
    try:
        return json.loads(js_obj)
    except:
        # 簡易的なクォート修正
        fixed = re.sub(r'(\w+)\s*:', r'"\1":', js_obj)
        try:
            return json.loads(fixed)
        except:
            return None

def save_problems_data(path: str, data: dict):
    """整理されたデータを保存する"""
    # 元のファイル形式を尊重
    dir_path = os.path.join(PROBLEMS_DIR, path)
    if os.path.isdir(dir_path):
        file_path = os.path.join(dir_path, "data.js")
    else:
        file_path = os.path.join(PROBLEMS_DIR, f"{path}.js")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    content = f"""// Auto-organized problem data
window.practiceData = window.practiceData || {{}};
window.practiceData["{path}"] = {json_str};
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [SAVED] {file_path}")

# ============================================================
# 分類ロジック
# ============================================================

def organize_file(path: str):
    print(f"\n[Processing] {path}")
    data = load_problems_for_path(path)
    if not data or "chapters" not in data:
        print(f"  [SKIP] No data found for {path}")
        return

    # 全てのレッスンをフラットにする
    all_lessons = []
    for ch in data["chapters"]:
        for lesson in ch.get("lessons", []):
            all_lessons.append(lesson)

    if not all_lessons:
        print(f"  [SKIP] No lessons found in {path}")
        return

    print(f"  Found {len(all_lessons)} lessons. Asking Qwen for classification...")

    # Qwen へのプロンプト構築
    # 15問ずつバッチ処理する（トークン制限と精度のバランス）
    batch_size = 15
    new_lesson_map = {} # id -> new_chapter_title

    is_fill = "short_fill" in path
    
    for i in range(0, len(all_lessons), batch_size):
        batch = all_lessons[i:i+batch_size]
        
        problem_descriptions = []
        for l in batch:
            desc = f"ID: {l['id']}\nTitle: {l['title']}\nInstruction: {l['instruction']}\nContent: {l.get('content', '')}\nAnswers: {', '.join(l.get('answers', []))}"
            problem_descriptions.append(desc)

        if is_fill:
            category_guide = "空欄補充問題です。『時制』『関係詞』『比較』『助動詞』『前置詞』『接続詞』『不定詞・動名詞』『分詞』などの文法項目、または『語彙』『熟語』の中から、最も適切な分類を1つ選んでください。"
        else:
            category_guide = "長文読解または和訳問題です。『科学・技術』『社会・経済』『文化・歴史』『日常生活』『環境・自然』『心理・教育』などのテーマから、最も適切な分類を1つ選んでください。"

        prompt = f"""あなたは英語教育の専門家です。以下の英語の問題リストを分析し、各問題に最適な『単元名（チャプター名）』を決定してください。

【分類の指針】
{category_guide}
※既存の分類にとらわれず、内容から判断してください。

【問題リスト】
{chr(10).join(problem_descriptions)}

【出力形式】
JSON形式で、IDをキー、単元名を値として出力してください。
例: {{"ID-001": "単元名", "ID-002": "単元名"}}
"""

        try:
            response = call_ollama(prompt)
            classification = parse_llm_response(response)
            new_lesson_map.update(classification)
            print(f"  Processed batch {i//batch_size + 1}")
        except Exception as e:
            print(f"  [ERROR] Batch processing failed: {e}")

    # 分類結果に基づいて再構成
    organized_chapters = {}
    for lesson in all_lessons:
        new_ch_title = new_lesson_map.get(lesson["id"], "未分類")
        if new_ch_title not in organized_chapters:
            organized_chapters[new_ch_title] = []
        organized_chapters[new_ch_title].append(lesson)

    # chapters 配列を作成
    new_chapters = []
    for title, lessons in organized_chapters.items():
        new_chapters.append({
            "title": title,
            "lessons": lessons
        })

    # タイトルでソート（見栄えのため）
    new_chapters.sort(key=lambda x: x["title"])

    data["chapters"] = new_chapters
    save_problems_data(path, data)

def main():
    parser = argparse.ArgumentParser(description="English problems organizer using Qwen")
    parser.epilog = "Example: python organize_english_problems.py --path english/short_fill/level_1"
    parser.add_argument("--path", type=str, help="Specific path to organize (e.g. english/short_fill/level_1)")
    parser.add_argument("--all", action="store_true", help="Organize all English problems")
    
    args = parser.parse_args()

    if args.path:
        organize_file(args.path)
    elif args.all:
        # english 以下の全ファイルを探索
        for root, dirs, files in os.walk(os.path.join(PROBLEMS_DIR, "english")):
            for file in files:
                if file.endswith(".js"):
                    # 相対パスを取得
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, PROBLEMS_DIR)
                    # 拡張子を除去
                    path_slug = rel_path.replace("\\", "/").replace(".js", "")
                    if path_slug.endswith("/data"):
                        path_slug = path_slug[:-5]
                    
                    organize_file(path_slug)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
