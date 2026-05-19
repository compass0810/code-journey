import google.generativeai as genai
import os

# APIキーを直接入れるか、環境変数から取得
api_key = os.getenv("GEMINI_API_KEY", "AIzaSyDWECPPrJ3tXKxxJ0AMFKPyBadBzTVJl04")
genai.configure(api_key=api_key)

print("利用可能なモデル一覧:")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f" - {m.name}")
except Exception as e:
    print(f"エラーが発生しました: {e}")
