import os
import json
import re

PROBLEMS_DIR = "problems/math"

# 翻訳辞書
TRANSLATION_MAP = {
    "math_1": "数学I",
    "math_2": "数学II",
    "math_3": "数学III",
    "math_a": "数学A",
    "math_b": "数学B",
    "math_c": "数学C",
    "numbers_and_expressions": "数と式",
    "real_numbers": "実数",
    "calculation": "計算",
    "inequalities": "不等式",
    "logic_and_sets": "集合と論理",
    "sets": "集合",
    "logic": "論理",
    "quadratics": "2次関数",
    "graph": "グラフ",
    "equations_inequalities": "方程式・不等式",
    "trigonometry": "三角比",
    "acute": "鋭角の三角比",
    "extension": "三角比の拡張",
    "application": "応用",
    "data_analysis": "データの分析",
    "variance": "分散と標準偏差",
    "correlation": "相関関係",
    "integers": "整数の性質",
    "euclidean": "ユークリッドの互除法",
    "base_n": "n進法",
    "permutations_combinations": "順列・組合せ",
    "probability": "確率",
    "independent_trials": "独立な試行",
    "conditional": "条件付き確率",
    "geometry": "図形の性質",
    "triangle": "三角形の性質",
    "circle": "円の性質",
    "sequence": "数列",
    "progression": "等差・等比数列",
    "sum": "数列の和",
    "induction": "数学的帰納法",
    "exponential_logarithmic": "指数関数・対数関数",
    "exponential": "指数関数",
    "logarithmic": "対数関数",
    "trig_functions": "三角関数",
    "addition_theorem": "加法定理",
    "differentiation": "微分法",
    "differentiation_apps": "微分法の応用",
    "derivatives": "導関数",
    "integration": "積分法",
    "integration_apps": "積分法の応用",
    "indefinite": "不定積分",
    "definite": "定積分",
    "functions_limits": "関数と極限",
    "function_limits": "関数の極限",
    "sequence_limits": "数列の極限",
    "various": "諸関数",
    "limits": "極限",
    "vectors": "ベクトル",
    "plane": "平面ベクトル",
    "space": "空間ベクトル",
    "complex_plane": "複素数平面",
    "quadratic_curves": "2次曲線",
    "matrices": "行列",
    "representation": "表現",
    "increase_decrease": "増減・極値",
    "basics": "基礎",
    "polar_coordinates": "極座標",
    "parametric": "媒介変数表示",
    "statistics": "統計",
    "distribution": "分布",
    "differentiation_applications": "微分法の応用",
    "integration_applications": "積分法の応用",
    "sequences": "数列",
    "counts": "数え上げ",
    "curves": "曲線",
    "quadrics": "2次曲線",
    "probability": "確率",
    "math": "数学",
    "functions": "関数",
    "triangles": "三角形",
    "human_activity": "人間の活動",
    "living": "生活",
    "differentiation_apps": "微分法の応用",
    "integration_apps": "積分法の応用",
    "circles": "円の性質",
    "addition": "加法定理",
    "proof": "証明",
    "equations_proof": "式と証明",
}

def translate_title(title):
    # パス形式の場合 (e.g. "math_3 / differentiation / derivatives")
    if "/" in title:
        parts = [p.strip() for p in title.split("/")]
        # 最後の要素を取得
        last_part = parts[-1]
        return TRANSLATION_MAP.get(last_part, last_part)
    
    # 単一の英単語の場合
    return TRANSLATION_MAP.get(title, title)

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # window.practiceData["path"] = { ... }; の形式を抽出
    match = re.search(r"(window\.practiceData\[\".*\"\]\s*=\s*)({.*});", content, re.DOTALL)
    if not match:
        return False
    
    prefix = match.group(1)
    json_str = match.group(2)
    
    try:
        data = json.loads(json_str)
        modified = False
        
        if "chapters" in data:
            for chapter in data["chapters"]:
                original_title = chapter.get("title", "")
                translated_title = translate_title(original_title)
                
                if original_title != translated_title:
                    chapter["title"] = translated_title
                    modified = True
                    print(f"  [Translated] {original_title} -> {translated_title}")
        
        if modified:
            new_json = json.dumps(data, indent=4, ensure_ascii=False)
            new_content = content[:match.start()] + prefix + new_json + ";" + content[match.end():]
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True
            
    except Exception as e:
        print(f"  [Error] Failed to process {file_path}: {e}")
        
    return False

def main():
    print("数学単元名の翻訳を開始します...")
    count = 0
    for root, dirs, files in os.walk(PROBLEMS_DIR):
        for file in files:
            if file.endswith(".js"):
                file_path = os.path.join(root, file)
                if process_file(file_path):
                    count += 1
                    
    print(f"\n[完了] {count} 個のファイルを更新しました。")

if __name__ == "__main__":
    main()
