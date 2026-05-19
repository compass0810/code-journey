import base64
import json
import os
import re
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# 設定
GEMINI_API_KEY = "AIzaSyDWECPPrJ3tXKxxJ0AMFKPyBadBzTVJl04"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemma-4-31b-it')

PROGRESS_FILE = 'user_progress.json'

@app.route('/')
def index():
    return send_from_directory(os.path.abspath('.'), 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(os.path.abspath('.'), path)

@app.route('/save_progress', methods=['POST'])
def save_progress():
    try:
        data = request.json
        with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/load_progress', methods=['GET'])
def load_progress():
    try:
        if os.path.exists(PROGRESS_FILE):
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                return jsonify(json.load(f))
        return jsonify({"progress": {}, "results": {}})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/grade', methods=['POST'])
def grade():
    try:
        data = request.json
        problem = data.get('problem', {})
        answer = data.get('answer', '')
        is_image = data.get('is_image', False)
        level = data.get('level', 'level_A')
        # レベルに応じた満点の設定
        level_max_scores = {
            'level_A': 5,
            'level_B': 10,
            'level_C': 20,
            'level_D': 30
        }
        max_score = level_max_scores.get(level, 100)

        # プロンプトの構築
        prompt = f"""
あなたは教育の専門家です。以下の問題に対する生徒の解答を採点し、詳細なフィードバックをJSON形式で返してください。

【問題情報】
タイトル: {problem.get('title')}
問題の指示: {problem.get('instruction')}
問題の内容: {problem.get('content')}
正解例: {', '.join(problem.get('answers', [])) if isinstance(problem.get('answers'), list) else problem.get('answers')}
レベル: {level} (満点: {max_score}点)

【生徒の解答】
{'(画像データが送信されました。画像内の内容を読み取って採点してください)' if is_image else answer}

【採点・評価基準】
- S: 完璧。非の打ち所がない解答。満点の {max_score} 点を付与。
- A: ほぼ正解。些細なミスはあるが、概念の理解は十分。{int(max_score * 0.8)}〜{max_score-1} 点程度。
- B: 半分以上正解。重要なポイントは押さえている。{int(max_score * 0.6)}〜{int(max_score * 0.7)} 点程度。
- C: 不十分。理解が不足している。{int(max_score * 0.4)}〜{int(max_score * 0.5)} 点程度。
- D: ほとんど白紙、または全く的外れな解答。{int(max_score * 0.2)}点以下。

【出力形式 (必ず以下のJSON構造のみを返してください。説明文は不要です)】
{{
  "score": 0〜{max_score}の数値,
  "evaluation": "S", "A", "B", "C", "D" のいずれか,
  "commentary": {{
    "good_points": "解答の中で評価できる具体的な点",
    "bad_points": "間違いや改善が必要な具体的な点",
    "advice": "今後どのように学習すべきかのアドバイス",
    "solution": "理想的な解答例とその解説（改行は\\nを使用）"
  }}
}}
"""

        if is_image:
            # base64画像の処理
            if ',' in answer:
                header, encoded = answer.split(",", 1)
            else:
                encoded = answer
            image_data = base64.b64decode(encoded)
            response = model.generate_content([
                prompt,
                {'mime_type': 'image/png', 'data': image_data}
            ])
        else:
            response = model.generate_content(prompt)

        # レスポンスからJSONを抽出
        text = response.text
        json_match = re.search(r'(\{[\s\S]*\})', text)
        if json_match:
            result = json.loads(json_match.group(1))
            return jsonify(result)
        else:
            print("AI Response:", text)
            raise Exception("AIからのレスポンスをJSONとして解析できませんでした。")

    except Exception as e:
        import traceback
        traceback.print_exc()
        print("Error in /grade:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # ローカルネットワーク内からのアクセスを許可
    app.run(host='0.0.0.0', port=5000, debug=True)
