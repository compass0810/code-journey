import re

def get_math_units():
    return {
        "math_1": {
            "title": "数学I",
            "units": {
                "numbers_and_expressions": ("数と式", ["calculation", "real_numbers", "inequalities"]),
                "logic_and_sets": ("集合と論証", ["sets", "logic"]),
                "quadratics": ("2次関数", ["graph", "equations_inequalities"]),
                "trigonometry": ("図形と計量", ["acute", "extension", "application"]),
                "data_analysis": ("データの分析", ["variance", "correlation", "application"])
            }
        },
        "math_a": {
            "title": "数学A",
            "units": {
                "probability": ("場合の数と確率", ["sets", "counts", "basics", "various"]),
                "geometry": ("図形の性質", ["triangles", "circles", "solid"]),
                "human_activity": ("数学と人間の活動", ["living", "enjoying"])
            }
        },
        "math_2": {
            "title": "数学II",
            "units": {
                "equations_proof": ("式と証明", ["calculation", "quadratics", "higher", "proof"]),
                "coordinates": ("図形と方程式", ["lines", "circles", "loci"]),
                "trigonometry": ("三角関数", ["functions", "addition"]),
                "exponential_log": ("指数関数・対数関数", ["exponential", "logarithmic"]),
                "calculus": ("微分と積分", ["differentiation", "integration"])
            }
        },
        "math_b": {
            "title": "数学B",
            "units": {
                "sequences": ("数列", ["basics", "induction"]),
                "statistics": ("統計的な推測", ["sampling", "distribution", "normal", "inference"]),
                "society": ("数学と社会生活", ["phenomena"])
            }
        },
        "math_3": {
            "title": "数学III",
            "units": {
                "functions_limits": ("関数と極限", ["functions", "sequence_limits", "function_limits"]),
                "differentiation": ("微分法", ["basics", "derivatives"]),
                "differentiation_apps": ("微分法の応用", ["increase_decrease", "various"]),
                "integration": ("積分法", ["indefinite", "definite", "applications"])
            }
        },
        "math_c": {
            "title": "数学C",
            "units": {
                "vectors": ("ベクトル", ["plane", "application", "space"]),
                "curves": ("平面上の曲線", ["quadrics", "polar"]),
                "complex_plane": ("複素数平面", ["basics", "application"]),
                "representation": ("数学的な表現の工夫", ["matrices", "data"])
            }
        }
    }

def generate_js_tree():
    levels = {
        "level_A": "レベルA（基本・標準）",
        "level_B": "レベルB（発展）",
        "level_C": "レベルC（共通テスト）",
        "level_D": "レベルD（二次試験）"
    }
    
    def get_levels_js(indent):
        res = "{\n"
        for i, (k, v) in enumerate(levels.items()):
            comma = "," if i < len(levels) - 1 else ""
            res += f'{indent}    "{k}": {{ title: "{v}", type: "course", mode: "practice", children: {{}} }}{comma}\n'
        res += indent + "}"
        return res

    math_data = get_math_units()
    
    js = 'const rootData = {\n    title: "CodeJourney",\n    type: "directory",\n    children: {\n'
    
    # Programming (Static for now)
    js += '        "programming": {\n            title: "プログラミング",\n            description: "Web開発やアプリ開発の基礎を学びます。",\n            type: "directory",\n            children: {\n                "html": {\n                    type: "course",\n                    mode: "learning",\n                    id: "html",\n                    title: "HTML & CSS 基礎",\n                    description: "ウェブページの骨組みを作り、美しく装飾するための言語を学びます。",\n                    chapters: []\n                }\n            }\n        },\n'
    
    # English
    js += '        "english": {\n            title: "英語",\n            type: "directory",\n            children: {\n'
    english_cats = [
        ("short_fill", "短文空欄補充"),
        ("long_reading", "長文読解"),
        ("translation_ej", "英文和訳"),
        ("translation_je", "和文英訳")
    ]
    for k, v in english_cats:
        js += f'                "{k}": {{\n                    title: "{v}",\n                    type: "directory",\n                    children: {get_levels_js("                    ")}\n                }},\n'
    js = js.rstrip(',\n') + '\n            }\n        },\n'
    
    # Math
    js += '        "math": {\n            title: "数学",\n            type: "directory",\n            children: {\n'
    for m_id, m_info in math_data.items():
        js += f'                "{m_id}": {{\n                    title: "{m_info["title"]}",\n                    type: "directory",\n                    children: {{\n'
        for u_id, u_info in m_info["units"].items():
            u_title, sub_units = u_info
            js += f'                        "{u_id}": {{\n                            title: "{u_title}",\n                            type: "directory",\n                            children: {{\n'
            for sub_id in sub_units:
                # Sub-unit titles are tricky, let's just use IDs for now or a map
                # Actually, I'll just use titles from my previous memory or just ID for now
                js += f'                                "{sub_id}": {{ title: "{sub_id}", type: "directory", children: {get_levels_js("                                ")} }},\n'
            js = js.rstrip(',\n') + '\n                            }\n                        },\n'
        js = js.rstrip(',\n') + '\n                    }\n                },\n'
    js = js.rstrip(',\n') + '\n            }\n        }\n    }\n};'
    
    return js

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_root_data = generate_js_tree()
    
    # Replace from const rootData = { ... to const app = {
    # Note: I need to preserve the actual content of chapters in HTML course if any.
    # Actually, I'll just keep the programming part as is in the script.
    
    # Let's just find the whole block and replace it.
    pattern = r'const rootData = \{[\s\S]*?\};'
    html = re.sub(pattern, new_root_data, html)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Regenerated rootData in index.html")

if __name__ == '__main__':
    main()
