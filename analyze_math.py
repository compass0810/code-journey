import os, json, re
import sys

sys.stdout.reconfigure(encoding='utf-8')

math_dir = r'c:\Users\compass\Documents\ProgrammingLearner\html_version\problems\math'

all_lessons = []
for root, dirs, files in os.walk(math_dir):
    for f in files:
        if f == 'data.js':
            path = os.path.join(root, f)
            rel = os.path.relpath(root, r'c:\Users\compass\Documents\ProgrammingLearner\html_version\problems').replace(os.sep, '/')
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()
            match = re.search(r'window\.practiceData\[.*?\] = ({.*});', content, re.DOTALL)
            if not match:
                continue
            try:
                data = json.loads(match.group(1))
            except Exception as e:
                print(f"JSON parse error in {rel}: {e}")
                continue
            for ch in data.get('chapters', []):
                for lesson in ch.get('lessons', []):
                    all_lessons.append({
                        'path': rel,
                        'file': path,
                        'id': lesson.get('id',''),
                        'serial': lesson.get('serial_number',''),
                        'title': lesson.get('title',''),
                        'answers': lesson.get('answers', []),
                        'matchType': lesson.get('matchType', 'exact'),
                        'instruction': lesson.get('instruction', ''),
                    })

print(f'Total lessons: {len(all_lessons)}')

# Check duplicate by instruction (same problem content)
instr_map = {}
for l in all_lessons:
    key = l['instruction'].strip()
    if not key:
        continue
    if key not in instr_map:
        instr_map[key] = []
    instr_map[key].append(l)
dup_instr = {k: v for k, v in instr_map.items() if len(v) > 1}
print(f'\n=== Duplicate by instruction content: {len(dup_instr)} groups ===')
for k,v in list(dup_instr.items()):
    print(f'\n  Instruction (first 80 chars): "{k[:80]}"')
    for x in v:
        print(f'    id={x["id"]}')
        print(f'    serial={x["serial"]}, path={x["path"]}')
        print(f'    answers={x["answers"]}')

# Serial number analysis per subject - more detailed
print('\n=== Serial number details ===')
for subj in ['math_1', 'math_a', 'math_2', 'math_b', 'math_3', 'math_c']:
    lessons = [l for l in all_lessons if l['path'].startswith('math/' + subj + '/')]
    # Show serial numbers not matching subject name
    wrong_subj = []
    for l in lessons:
        if subj == 'math_1' and '数学I' not in l['serial']:
            wrong_subj.append(l)
        elif subj == 'math_a' and '数学A' not in l['serial']:
            wrong_subj.append(l)
        elif subj == 'math_2' and '数学II' not in l['serial']:
            wrong_subj.append(l)
        elif subj == 'math_b' and '数学B' not in l['serial']:
            wrong_subj.append(l)
        elif subj == 'math_3' and '数学III' not in l['serial']:
            wrong_subj.append(l)
        elif subj == 'math_c' and '数学C' not in l['serial']:
            wrong_subj.append(l)
    if wrong_subj:
        print(f'\n{subj} - Wrong subject in serial ({len(wrong_subj)} items):')
        for l in wrong_subj[:10]:
            print(f'  serial="{l["serial"]}", id={l["id"]}')
