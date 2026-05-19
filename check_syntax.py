import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# <script> タグの内容を抽出
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
for i, script in enumerate(scripts):
    print(f"Checking script block {i}...")
    # 簡易的な括弧バランスチェック
    stack = []
    for line_no, line in enumerate(script.split('\n'), 1):
        for char in line:
            if char in '{[(':
                stack.append((char, line_no))
            elif char in '}])':
                if not stack:
                    print(f"  Unexpected {char} at line {line_no}")
                    continue
                last_char, last_line = stack.pop()
                if (char == '}' and last_char != '{') or \
                   (char == ']' and last_char != '[') or \
                   (char == ')' and last_char != '('):
                    print(f"  Mismatched {char} at line {line_no} (opened {last_char} at line {last_line})")
    
    if stack:
        for char, line_no in stack:
            print(f"  Unclosed {char} opened at line {line_no}")
