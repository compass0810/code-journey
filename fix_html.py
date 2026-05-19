import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all empty children dicts with Level A~D
level_str = '''children: {
                                "level_A": { title: "レベルA（基本・標準）", type: "directory", children: {} },
                                "level_B": { title: "レベルB（発展）", type: "directory", children: {} },
                                "level_C": { title: "レベルC（共通テスト）", type: "directory", children: {} },
                                "level_D": { title: "レベルD（二次試験）", type: "directory", children: {} }
                            }'''

html = re.sub(r'children:\s*\{\}', level_str, html)

# For English section and math graph, they already had level_1 manually inserted. Let's just run regex to replace them
# Or better, since there are only a few, I'll let the script remove level_1 and replace it.
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
