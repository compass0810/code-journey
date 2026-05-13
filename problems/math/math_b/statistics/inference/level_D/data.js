window.practiceData = window.practiceData || {};
window.practiceData["math/math_b/statistics/inference/level_D"] = {
    "chapters": [
        {
            "title": "統計的な推測",
            "lessons": [
                {
                    "id": "math-math_b-statistics-inference-level_D-42e10201-e225-447c-a8bb-ba95656c10f0",
                    "title": "正規母集団における標本平均の信頼区間と定数の決定",
                    "instruction": "母平均m、母分散σ^2の正規母集団から大きさnの無作為標本を抽出し、その標本平均をXとする。母分散σ^2が未知であるため、不偏分散U^2を用いてmの信頼度95%の信頼区間を [X - k*U/sqrt(n), X + k*U/sqrt(n)] と定める。ここで、自由度n-1のt分布に従う確率変数Tに対し、P(-t_0.05 <= T <= t_0.05) = 0.95 となる値 t_0.05 を用いて、標本サイズnを無限大に大きくしたとき、k/t_0.05 が収束する値を求めよ。",
                    "answers": [
                        "1"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学B No.90",
                    "subject_display": "数学B",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_b-statistics-inference-level_D-69ee3065-f7e9-445b-8948-e6c7edecfa64",
                    "serial_number": "数学B No.91",
                    "title": "母平均の推定と信頼区間の包含関係",
                    "instruction": "ある正規分布 N(μ, 16) に従う母集団から抽出された大きさ n の無作為標本について、母平均 μ の信頼度95%の信頼区間を [X_bar - 1.96 * 4 / sqrt(n), X_bar + 1.96 * 4 / sqrt(n)] とする。この信頼区間の幅を 0.8 以下にするために必要な標本サイズ n の最小値を求めよ。ただし、sqrt(n) は n の平方根を表す。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "385"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_b-statistics-inference-level_D-02ea916f-bf61-4a73-a698-7fd6e3f4e567",
                    "serial_number": "数学B No.92",
                    "title": "母平均の区間推定と標本サイズの決定",
                    "instruction": "ある工場で製造される製品の重量Xは、正規分布N(μ, σ^2)に従う。過去のデータから母標準偏差σ = 5であることは既知である。\nこの製品から無作為にn個の標本を抽出し、その標本平均をX_barとする。母平均μに対する信頼度95%の信頼区間を[X_bar - L, X_bar + L]とする。\nこのとき、信頼区間の幅2Lが0.5以下となるために必要な標本サイズnの最小値を求めよ。ただし、標準正規分布においてP(|Z| ≦ 1.96) = 0.95とする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "385"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.6
                },
                {
                    "id": "math-math_b-statistics-inference-level_D-861d5d71-5084-4d19-8015-c3594ad9c6b0",
                    "serial_number": "数学B No.145",
                    "subject_display": "数学B",
                    "title": "標本平均を用いた母平均の推定と信頼区間",
                    "instruction": "母集団が正規分布N(μ, 16)に従うとき、大きさnの無作為標本を抽出し、その標本平均をXとする。母平均μに対する信頼度95%の信頼区間[X-d, X+d]の長さ2dが0.5以下となるために必要な最小の標本サイズnを求めよ。ただし、標準正規分布の上側5%点は1.645、上側2.5%点は1.96とし、必要であれば√を用いて答えよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "246"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.7
                },
                {
                    "id": "math-math_b-statistics-inference-level_D-4aa83db9-5e6c-4b1c-bed0-6eca6758a5c7",
                    "serial_number": "数学B No.173",
                    "subject_display": "数学B",
                    "title": "母平均の推定と信頼区間の包含関係",
                    "instruction": "ある正規分布 N(μ, 16) に従う母集団から抽出された大きさ n の無作為標本について、標本平均を X̄ とする。母平均 μ に対する信頼度 95% の信頼区間を [X̄ - a, X̄ + a] としたとき、以下の問いに答えよ。\n\n1. 標本サイズ n を 16 としたとき、信頼区間が母平均 μ を含む確率が 0.95 となるような正の定数 a を求めよ。（ただし、標準正規分布の上側 2.5% 点を 1.96 とする。）\n\n2. 信頼区間の幅 2a が 1.0 以下となるような最小の自然数 n を求めよ。\n\n3. 標本サイズ n が 100 のとき、母平均 μ が [X̄ - 0.5, X̄ + 0.5] に含まれる確率を、標準正規分布表を用いて求めよ。（ただし、1.96 / √n の値を考慮すること。）",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "1. 1.96, 2. 246, 3. 0.9544"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.5
                }
            ]
        },
        {
            "title": "推測統計",
            "lessons": [
                {
                    "id": "math-math_b-statistics-inference-level_D-751b2bd7-30c5-46b5-a46f-16e4b8b06f02",
                    "serial_number": "数学B No.93",
                    "title": "母平均の推定と信頼区間の包含関係",
                    "instruction": "ある正規分布 N(μ, 16) に従う母集団から抽出された大きさ n の無作為標本平均を Xバー とする。母平均 μ の 95% 信頼区間 [Xバー - 1.96 * 4 / sqrt(n), Xバー + 1.96 * 4 / sqrt(n)] が、母平均 μ を含む確率が 0.95 以上となるような最小の自然数 n は存在するか。存在する場合はその値を求め、存在しない場合はその理由を述べよ。ただし、標準正規分布表において P(Z <= 1.96) = 0.975 とする。また、信頼区間の定義における n は母平均の推定精度に依存するものとする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "存在する（n=1）"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.5
                }
            ]
        }
    ]
};