import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'const rootData = (\{.*?\n        \});', html, re.DOTALL)
if not m:
    print("Could not find rootData")
else:
    s = m.group(1)
    lines = s.split('\n')
    open_brackets = 0
    close_brackets = 0
    for i, line in enumerate(lines):
        open_brackets += line.count('{')
        close_brackets += line.count('}')
        if close_brackets > open_brackets:
            print(f"Error at line {i+1}: {line}")
            break
    print(f"Total: open={open_brackets}, close={close_brackets}")
