import re

INDEX_FILE = "index.html"

# 翻訳辞書
TRANSLATION_MAP = {
    "sets": "集合",
    "logic": "論理",
    "calculation": "計算",
    "real_numbers": "実数",
    "inequalities": "不等式",
    "quadratics": "2次関数",
    "graph": "グラフ",
    "equations_inequalities": "方程式・不等式",
    "acute": "鋭角の三角比",
    "extension": "三角比の拡張",
    "application": "応用",
    "variance": "分散と標準偏差",
    "correlation": "相関関係",
    "euclidean": "ユークリッドの互除法",
    "base_n": "n進法",
    "counts": "数え上げ",
    "basics": "基本",
    "various": "諸関数",
    "triangles": "三角形の性質",
    "circles": "円の性質",
    "solid": "空間図形",
    "living": "生活の中の数学",
    "enjoying": "数学を楽しむ",
    "equations_proof": "式と証明",
    "higher": "高次方程式",
    "proof": "証明",
    "lines": "直線の方程式",
    "loci": "軌跡と領域",
    "functions": "関数",
    "addition": "加法定理",
    "exponential": "指数関数",
    "logarithmic": "対数関数",
    "differentiation": "微分法",
    "integration": "積分法",
    "induction": "数学的帰納法",
    "sampling": "標本調査",
    "distribution": "確率分布",
    "normal": "正規分布",
    "inference": "統計的な推測",
    "phenomena": "数学的な事象",
    "sequence_limits": "数列の極限",
    "function_limits": "関数の極限",
    "derivatives": "導関数",
    "increase_decrease": "関数の増減と極値",
    "indefinite": "不定積分",
    "definite": "定積分",
    "applications": "積分法の応用",
    "plane": "平面",
    "space": "空間",
    "quadrics": "2次曲線",
    "polar": "極座標と極方程式",
    "matrices": "行列",
    "data": "データの活用",
}

def main():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # title: "english_name" を検索して置換
    def replace_func(match):
        eng_name = match.group(1)
        if eng_name in TRANSLATION_MAP:
            return f'title: "{TRANSLATION_MAP[eng_name]}"'
        return match.group(0)

    # 引用符がダブルクォートの場合
    new_content = re.sub(r'title:\s*"([^"]+)"', replace_func, content)
    # 引用符がシングルクォートの場合
    new_content = re.sub(r"title:\s*'([^']+)'", lambda m: f"title: '{TRANSLATION_MAP.get(m.group(1), m.group(1))}'", new_content)

    if new_content != content:
        with open(INDEX_FILE, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"{INDEX_FILE} を更新しました。")
    else:
        print(f"{INDEX_FILE} に変更はありませんでした。")

if __name__ == "__main__":
    main()
