import os
import re
import json

problems_dir = r"c:\Users\compass\Documents\ProgrammingLearner\html_version\problems\english"
titles = set()

for root, dirs, files in os.walk(problems_dir):
    for file in files:
        if file == "data.js":
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Simple regex to find chapter titles
                matches = re.findall(r'"title":\s*"([^"]+)"', content)
                for m in matches:
                    titles.add(m)

for t in sorted(list(titles)):
    print(t)
