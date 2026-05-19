import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html = f.read()

        m = re.search(r'const rootData = (\{.*?\n        \});', html, re.DOTALL)
        if not m:
            print("Could not find rootData")
            return
            
        data = m.group(1)
        
        data_json = re.sub(r'([a-zA-Z0-9_]+)\s*:', r'"\1":', data)
        data_json = data_json.replace("'", '"')
        data_json = re.sub(r',\s*}', '}', data_json)
        data_json = re.sub(r',\s*\]', ']', data_json)

        lines = data_json.split('\n')
        for i in range(15, 35):
            if i < len(lines):
                print(f"{i+1}: {lines[i]}")

    except Exception as e:
        print("JSON Error:", e)

if __name__ == '__main__':
    main()
