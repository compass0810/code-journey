import requests
import json

url = "https://vvzwecgwkktysjltjeca.supabase.co/rest/v1/user_data"
headers = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ2endlY2d3a2t0eXNqbHRqZWNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzg2NzMzNTMsImV4cCI6MjA5NDI0OTM1M30._v9WOSFJAYQDBjbGY2aoZN43JD_QvB-r_xgTWJBP5M0",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ2endlY2d3a2t0eXNqbHRqZWNhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzg2NzMzNTMsImV4cCI6MjA5NDI0OTM1M30._v9WOSFJAYQDBjbGY2aoZN43JD_QvB-r_xgTWJBP5M0"
}

try:
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        print("Existing Users in Supabase:")
        for row in data:
            print(f"- ID: {row.get('user_id')}, Last Updated: {row.get('updated_at')}, Has Data: {bool(row.get('data'))}")
    else:
        print("Error response:", response.text)
except Exception as e:
    print("Request failed:", e)
