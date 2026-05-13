window.practiceData = window.practiceData || {};
window.practiceData["math/math_b/statistics/distribution/level_D"] = {
    "chapters": [
        {
            "title": "確率分布",
            "lessons": [
                {
                    "id": "math-math_b-statistics-distribution-level_D-69949a5a-b10e-419f-b602-8ad27f64a574",
                    "title": "離散型確率分布における期待値の最小化",
                    "instruction": "ある変量Xが、値 1, 2, 3 をとり、それぞれの確率が P(X=1) = p, P(X=2) = 1-3p, P(X=3) = 2p であるとする。このとき、確率が負にならないためのpの範囲を求めよ。また、関数 f(k) = E(|X-k|^2) を最小にする実数kの値をpを用いて表し、その最小値を g(p) とする。pがとり得る値の範囲において、g(p) の最大値を求めよ。",
                    "answers": [
                        "1/12"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学B No.74",
                    "subject_display": "数学B",
                    "difficulty": 9.4
                },
                {
                    "id": "math-math_b-statistics-distribution-level_D-47105671-10f2-4ca3-95c0-7b988fc65e4d",
                    "serial_number": "数学B No.75",
                    "title": "確率変数の和の分散と条件付き確率",
                    "instruction": "ある箱の中に1からnまでの番号が書かれたカードが各1枚ずつ、計n枚入っている。この箱から1枚ずつ無作為に2回カードを取り出す試行を行う。1回目に取り出したカードの番号をX、2回目に取り出したカードの番号をYとする（ただし、1回目に取り出したカードは戻さないものとする）。このとき、確率変数Z = X + Y について、分散V(Z)をnを用いて表せ。また、Z = n + 1 となる確率をP_nとするとき、P_n = 1/10 となるようなnの値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "(n^2-1)/6, n=19"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.9
                },
                {
                    "id": "math-math_b-statistics-distribution-level_D-47ca8d6c-d5fd-4f0b-8770-bc7c2649d3e0",
                    "serial_number": "数学B No.76",
                    "title": "確率変数の期待値と分散の制約による定数決定",
                    "instruction": "ある確率変数 X は、値 0, 1, 2 をとり、それぞれの確率を P(X=0) = a, P(X=1) = b, P(X=2) = c とする。ここで a, b, c は正の定数であり、a + b + c = 1 を満たす。X の期待値が 1 であり、分散が 1/2 であるとき、定数 a, b, c の値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "a=1/4, b=1/2, c=1/4"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.6
                },
                {
                    "id": "math-math_b-statistics-distribution-level_D-13282008-d87f-4130-a573-8cc48d8c58cd",
                    "serial_number": "数学B No.169",
                    "subject_display": "数学B",
                    "title": "確率分布と期待値の最大化",
                    "instruction": "袋の中に1からnまでの番号が書かれたn枚のカードがある。この袋から1枚のカードを取り出し、書かれた数をXとする。さらに、Xが得られた後に、1からXまでの番号が書かれたX枚のカードが入った別の袋から1枚のカードを取り出し、その数をYとする。このとき、期待値E[Y]が最大となる最小の自然数nを求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "3"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.5
                }
            ]
        },
        {
            "title": "統計的な推測",
            "lessons": [
                {
                    "id": "math-math_b-statistics-distribution-level_D-856d85a1-5225-482d-8961-5db451093491",
                    "serial_number": "数学B No.77",
                    "title": "正規分布と確率変数の線形変換",
                    "instruction": "確率変数Xが正規分布N(m, σ^2)に従うとする。いま、新たな確率変数YをY = aX + b (a > 0) と定め、Yが標準正規分布N(0, 1)に従うものとする。このとき、Xの平均mと分散σ^2を用いて、aとbをmとσを用いて表せ。また、Xが区間[m-σ, m+σ]に含まれる確率がPであるとき、Yがとる値の範囲をPを用いて表せ（ただし、標準正規分布の累積分布関数をΦ(z)とする）。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "a=1/σ, b=-m/σ, [-Φ^{-1}((1+P)/2), Φ^{-1}((1+P)/2)]"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.2
                }
            ]
        },
        {
            "title": "正規分布",
            "lessons": [
                {
                    "id": "math-math_b-statistics-distribution-level_D-fa658f08-181b-4036-a396-05578363ebf3",
                    "serial_number": "数学B No.141",
                    "subject_display": "数学B",
                    "title": "正規分布と確率変数の最大値",
                    "instruction": "確率変数X_1, X_2, ..., X_nは互いに独立に、平均0、分散1の正規分布N(0, 1)に従うとする。M_n = max{X_1, X_2, ..., X_n}とおくとき、nが十分に大きいとき、M_nの期待値E[M_n]は近似的にどのような値に収束するか、あるいはどのような関数で表されるか。n → ∞ における漸近的な挙動を考察し、期待値 E[M_n] が log(n) を用いてどのような式で近似されるか答えよ。（ヒント: P(M_n ≦ x) = {Φ(x)}^n を用いて計算せよ）",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "sqrt(2log(n))"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.7
                }
            ]
        }
    ]
};