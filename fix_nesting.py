import re

def fix_nested_levels(text):
    # Find all occurrences of level_X followed by a directory with children
    # and replace them with empty children.
    # We look for something like: "level_A": { ... children: { ... } }
    # and replace with: "level_A": { ... children: {} }
    
    # Pattern to match the level nodes that have children
    # We use a non-greedy match for the content between children: { and the closing }
    # but we need to be careful about nested braces.
    
    # A safer way: identify lines starting with "level_A": etc. and if they have a non-empty children, fix them.
    lines = text.split('\n')
    fixed_lines = []
    in_level_node = False
    
    for line in lines:
        if re.search(r'"level_[A-D]":\s*{', line):
            # This is a level node line.
            # Replace children: { ... } with children: {} if it's on the same line or starts here
            if 'children: {' in line and not 'children: {}' in line:
                line = re.sub(r'children: \{.*?\}', 'children: {}', line)
            in_level_node = True
            fixed_lines.append(line)
        elif in_level_node and 'children: {' in line and not 'children: {}' in line:
            # We are inside a level node and found a children block start
            # Skip lines until the closing brace of THIS children block
            # But wait, the nesting I saw was:
            # "level_A": { ... children: {
            #    "level_A": ...
            # } }
            # So I should just look for lines that look like "level_A": ... children: { and fix them.
            pass
        else:
            fixed_lines.append(line)
            
    return '\n'.join(fixed_lines)

# Actually, a better approach: 
# Any node named "level_A" through "level_D" should ALWAYS have "children: {}" in our design.

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match level_X nodes and ensure children is empty
    # Pattern: "level_A": { title: "...", type: "directory", children: { ... } }
    # We'll use a recursive regex or just multiple passes.
    
    # Simple approach: Find "level_A": { ... children: { and replace until the next "level_A": or similar.
    # This is risky. 
    
    # Let's try to match the specific broken pattern:
    # "level_A": { title: "...", type: "directory", children: { ... level_A ... } }
    
    new_content = content
    for level in ['A', 'B', 'C', 'D']:
        pattern = r'("level_' + level + r'":\s*{[^}]*?children:\s*\{)\s*"level_A":[\s\S]*?}\s*(})'
        # This matches "level_A": { ... children: { "level_A": ... } }
        # We want to replace it with "level_A": { ... children: {} }
        new_content = re.sub(pattern, r'\1}\2', new_content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed nesting in index.html")

if __name__ == '__main__':
    main()
