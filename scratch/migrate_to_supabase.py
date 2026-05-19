import requests
import json
import sys

# ユーザーIDを引数から取得するか、デフォルトを設定
user_id = sys.argv[1] if len(sys.argv) > 1 else "compass0810" # デフォルト

url = "https://vvzwecgwkktysjltjeca.supabase.co/rest/v1/user_data"
headers = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ2endlY2d3a2t0eXNqbHRqZWNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzg2NzMzNTMsImV4cCI6MjA5NDI0OTM1M30._v9WOSFJAYQDBjbGY2aoZN43JD_QvB-r_xgTWJBP5M0",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ2endlY2d3a2t0eXNqbHRqZWNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzg2NzMzNTMsImV4cCI6MjA5NDI0OTM1M30._v9WOSFJAYQDBjbGY2aoZN43JD_QvB-r_xgTWJBP5M0",
    "Content-Type": "application/json",
    "Prefer": "resolution=merge-duplicates"
}

# ローカルの進捗データを読み込み
try:
    with open("user_progress.json", "r", encoding="utf-8") as f:
        local_data = json.load(f)
    print("Loaded local user_progress.json successfully.")
except Exception as e:
    print("Failed to read user_progress.json:", e)
    sys.exit(1)

# アップロード用データの構築
payload = {
    "user_id": user_id,
    "data": {
        "progress": local_data.get("progress", {}),
        "results": local_data.get("results", {})
    }
}

try:
    # upsertを実行 (HTTP POST + Prefer: resolution=merge-duplicates または upsert)
    # SupabaseのREST API (PostgREST) でupsertを行うには、Preferヘッダーに resolution=merge-duplicates もしくは return=representation を指定し、POSTします。
    # かつプライマリキー（user_id）の重複時は更新するようにします。
    headers["Prefer"] = "resolution=merge-duplicates"
    response = requests.post(url, headers=headers, json=payload)
    
    print("Upload Status Code:", response.status_code)
    if response.status_code in [200, 201, 204]:
        print(f"Successfully uploaded/synchronized local progress to Supabase user '{user_id}'!")
    else:
        print("Upload failed:", response.text)
except Exception as e:
    print("Upload request failed:", e)
