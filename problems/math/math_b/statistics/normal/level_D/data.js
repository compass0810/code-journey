window.practiceData = window.practiceData || {};
window.practiceData["math/math_b/statistics/normal/level_D"] = {
    "chapters": [
        {
            "title": "正規分布",
            "lessons": [
                {
                    "id": "math-math_b-statistics-normal-level_D-ce3fa507-6b43-49d2-9666-9732d3248801",
                    "title": "正規分布と定数決定",
                    "instruction": "確率変数Xが正規分布N(μ, σ^2)に従うとする。Xの標準化変数をZ = (X - μ)/σとするとき、任意の正の定数kに対し、P(μ - kσ ≦ X ≦ μ + kσ) = p_k が成り立つ。このとき、P(X ≧ μ + 2σ) = 0.0228 として、確率密度関数f(x)が f(μ + a) = f(μ - 2a) を満たすような正の定数aを求めよ。ただし、f(x)は正規分布の確率密度関数である。",
                    "answers": [
                        "2/3"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学B No.106",
                    "subject_display": "数学B",
                    "difficulty": 9.4
                },
                {
                    "id": "math-math_b-statistics-normal-level_D-46cf173d-8c97-4109-8a6e-9c13cb5d1ba5",
                    "serial_number": "数学B No.107",
                    "title": "正規分布と確率密度の最大値",
                    "instruction": "確率変数Xは平均m、分散σ^2の正規分布N(m, σ^2)に従う。確率密度関数をf(x)とする。ある定数k (> 0)に対し、区間[m-k, m+k]におけるf(x)の最小値をg(k)とするとき、f(m+k) = 2g(k)を満たすkをσを用いて表せ。ただし、正規分布の確率密度関数はf(x) = 1/(√(2π)σ) * exp(-(x-m)^2 / (2σ^2))とする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "σ*sqrt(2*log(2))"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_b-statistics-normal-level_D-6256c8ca-b504-415f-8229-7b4c268f4f22",
                    "serial_number": "数学B No.108",
                    "title": "正規分布と確率密度の最大値",
                    "instruction": "確率変数 X が正規分布 N(m, σ^2) に従うとき、その確率密度関数を f(x) とする。\nある定数 a (a > 0) に対して、X が区間 [m - aσ, m + aσ] に含まれる確率を P(a) とする。\nまた、f(x) の最大値を M とし、区間 [m - σ, m + σ] における f(x) の最小値を m' とする。\nこのとき、M/m' = e^k が成り立つような定数 k を求めよ。ただし、e は自然対数の底とする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "1/2"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_b-statistics-normal-level_D-6d2b0f7b-85f2-47e0-9a7c-869e78694276",
                    "serial_number": "数学B No.109",
                    "title": "正規分布と確率変数の最大値",
                    "instruction": "確率変数 X_1, X_2, ..., X_n が互いに独立に、いずれも正規分布 N(0, 1) に従うものとする。このとき、Y = max{X_1, X_2, ..., X_n} とおく。n=2 のとき、Y がとりうる値の範囲が [y, ∞) となる確率 P(Y≧y) を y の式で表し、P(Y≧1) の値を求めよ。ただし、標準正規分布の分布関数を Φ(x) = (1/sqrt(2π)) * ∫_{-∞}^{x} exp(-t^2/2) dt とする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "1 - Φ(1)^2"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.6
                },
                {
                    "id": "math-math_b-statistics-normal-level_D-f6c360ab-9f69-4e35-9c2d-d08122679980",
                    "serial_number": "数学B No.149",
                    "subject_display": "数学B",
                    "title": "正規分布と確率密度の最大値",
                    "instruction": "確率変数Xが正規分布N(μ, σ^2)に従うとする。このとき、確率密度関数f(x) = (1/(√(2π)σ)) * exp(-(x-μ)^2 / (2σ^2)) について考える。ある実数aに対して、P(μ-a ≦ X ≦ μ+a) = 0.9545 を満たす定数aをσを用いて表せ。ただし、標準正規分布表よりP(|Z| ≦ 1) ≒ 0.6827、P(|Z| ≦ 2) ≒ 0.9545 であることを用いてよい。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "a = 2σ"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_b-statistics-normal-level_D-fc1db777-7a02-49be-a7fe-00084bcf102a",
                    "serial_number": "数学B No.177",
                    "subject_display": "数学B",
                    "title": "正規分布と標本平均の評価",
                    "instruction": "母集団が正規分布N(m, 16)に従うとき、大きさnの無作為標本をとる。標本平均をX_barとし、|X_bar - m| ≦ 0.4 となる確率が0.95以上となるような最小の自然数nを求めよ。\nなお、標準正規分布N(0, 1)に従う変数Zについて、P(|Z| ≦ 1.96) = 0.95 とする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "385"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.5
                }
            ]
        }
    ]
};