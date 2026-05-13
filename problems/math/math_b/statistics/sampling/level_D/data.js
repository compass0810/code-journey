window.practiceData = window.practiceData || {};
window.practiceData["math/math_b/statistics/sampling/level_D"] = {
    "chapters": [
        {
            "title": "統計的な推測",
            "lessons": [
                {
                    "id": "math-math_b-statistics-sampling-level_D-a6e4dd87-b6b3-461e-a2af-7338f80d48e7",
                    "title": "標本平均の分布と信頼区間の論証",
                    "instruction": "母集団が正規分布N(μ, 1)に従うとき、大きさnの無作為標本を抽出して得られる標本平均をX_barとする。このとき、標本平均の実現値x_barを用いて母平均μに対する信頼度95%の信頼区間を[x_bar - k, x_bar + k]と定める。信頼度95%に対応する標準正規分布の値を1.96とするとき、この信頼区間の幅が0.1以下となるために必要な標本サイズnの最小値を求めよ。",
                    "answers": [
                        "1537"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学B No.122",
                    "subject_display": "数学B",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_b-statistics-sampling-level_D-22041c15-2f44-4cf6-98b6-991f8729d87f",
                    "serial_number": "数学B No.123",
                    "title": "標本平均と信頼区間の最適化",
                    "instruction": "母標準偏差がσである母集団から、大きさnの無作為標本を抽出して母平均mの信頼度95%の信頼区間を求める。このとき、信頼区間の幅が母標準偏差σの0.5倍以下となるために必要な標本数nの最小値を求めよ。ただし、標準正規分布において-1.96から1.96までの確率を0.95とし、nは十分大きく正規分布で近似できるものとする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "62"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_b-statistics-sampling-level_D-dfc2235b-fe32-41f8-83da-a2550a0abf65",
                    "serial_number": "数学B No.124",
                    "title": "標本平均と信頼区間の最適化",
                    "instruction": "母標準偏差がσである母集団から、大きさnの無作為標本を抽出して母平均mの信頼度95%の信頼区間を求める。このとき、信頼区間の幅が母標準偏差σの0.4倍以下となるために必要な最小の標本サイズnを求めよ。ただし、標準正規分布において-1.96から1.96までの確率を0.95とし、nは正の整数とする。\n（※信頼区間の幅とは、信頼区間の上限と下限の差のことである）",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "97"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 10.2
                },
                {
                    "id": "math-math_b-statistics-sampling-level_D-964a9eef-14d8-48d4-8af3-d508f0d343af",
                    "serial_number": "数学B No.125",
                    "title": "標本平均と信頼区間の論証",
                    "instruction": "母平均m、母分散σ^2の母集団から大きさnの無作為標本を抽出し、その標本平均をX_barとする。標本平均の分布を正規分布N(m, σ^2/n)とみなすことができるとき、母平均mに対する信頼度95%の信頼区間[X_bar - k・σ/sqrt(n), X_bar + k・σ/sqrt(n)]を考える。ここで、標準正規分布に従う確率変数ZについてP(|Z| ≦ k) = 0.95を満たす正の定数kを1.96とする。\n母平均mを推定する際、信頼区間の幅を標本標準偏差σ/sqrt(n)の長さの2倍以下、かつ信頼区間の長さが0.1以下となるように標本の大きさnを決定したい。母標準偏差σ=1であるとき、この条件を満たす最小の自然数nを求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "385"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 10.5
                },
                {
                    "id": "math-math_b-statistics-sampling-level_D-e461c261-d61a-408d-8977-16b92035ebd6",
                    "serial_number": "数学B No.153",
                    "subject_display": "数学B",
                    "title": "標本平均と信頼区間の確率論的考察",
                    "instruction": "母平均m、母標準偏差σ（σ>0）の母集団から、大きさnの無作為標本を抽出して得られる標本平均をX_barとする。標本平均の期待値E(X_bar)=m、分散V(X_bar)=σ^2/nであることは既知とする。母平均mに対する信頼度95%の信頼区間[X_bar - k・σ/sqrt(n), X_bar + k・σ/sqrt(n)]を考える。中心極限定理により、nが十分に大きいとき、(X_bar - m) / (σ/sqrt(n)) は近似的に標準正規分布N(0, 1)に従うものとする。ここで、標準正規分布の上側5%点（P(Z > 1.645) = 0.05）および上側2.5%点（P(Z > 1.96) = 0.025）を用いて考える。いま、標本サイズnを固定したとき、信頼区間の幅L = 2k・σ/sqrt(n) について、Lが母平均mに対してある一定の精度以下となる確率を評価したい。標本サイズnを n ≧ (z・σ/d)^2 としたとき、信頼区間の幅Lがd以下となる確率が0.95となるような係数zの値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "1.96"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.8
                },
                {
                    "id": "math-math_b-statistics-sampling-level_D-8b745fc4-c159-4865-be48-e1b49b82e0a7",
                    "serial_number": "数学B No.181",
                    "subject_display": "数学B",
                    "title": "標本平均と信頼区間の論証",
                    "instruction": "母平均m、母分散σ^2の母集団から大きさnの無作為標本を抽出し、その標本平均をXとする。母分散σ^2が未知であり、標本から得られる不偏分散U^2を用いてmの信頼度95%の信頼区間を[X - c*U/sqrt(n), X + c*U/sqrt(n)]と定める。標本数nが十分に大きいとき、正規分布に従う確率変数Z = (X - m) / (U/sqrt(n)) の分布を標準正規分布で近似する。このとき、信頼区間の幅が母平均mの推定値の精度に与える影響を考察する。信頼区間の幅が標本平均Xの10%以下になるような標本数nの最小値を、標準正規分布のパーセント点 z_{0.025} = 1.96 を用いて、標本標準偏差s = sqrt(U^2) と標本平均Xの比率 k = s/|X| を用いて表せ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "n >= (39.2k)^2"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.5
                }
            ]
        }
    ]
};