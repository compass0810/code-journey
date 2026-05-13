window.practiceData = window.practiceData || {};
window.practiceData["math/math_a/probability/counts/level_D"] = {
    "chapters": [
        {
            "title": "数学A：確率",
            "lessons": [
                {
                    "id": "math-math_a-probability-counts-level_D-aadde59e-f1a2-4625-ae8d-b3112230b6fa",
                    "title": "硬貨の投げ上げと確率の極限的な推移",
                    "instruction": "1枚の硬貨を投げ、表が出れば+1点、裏が出れば-1点を得るゲームを行う。点数が0点からスタートし、n回投げ終えた時点での点数をX_nとする。各n(n=1, 2, ...)について、X_n = 0 となる確率をp_nとする。このとき、p_2, p_4を求めよ。また、p_{2n}をnを用いて表せ。（※nは正の整数とする）",
                    "answers": [
                        "p_2=1/2, p_4=3/8, p_{2n} = (2n)! / (4^n * (n!)^2)"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学A No.135",
                    "subject_display": "数学A",
                    "difficulty": 10.5
                },
                {
                    "id": "math-math_a-probability-counts-level_D-032609ad-c888-4c19-9d92-1ff3f089d657",
                    "serial_number": "数学A No.136",
                    "title": "カードの並べ替えと確率の最大化",
                    "instruction": "1からnまでの番号が書かれたn枚のカードがある。これらを1列に並べたとき、番号iのカードがi番目（左から数えてi番目）に置かれない確率をPnとする。ただし、n≧2とする。\n(1) Pnをnを用いて表せ。\n(2) n枚のカードをランダムに並べ替える試行を繰り返すとき、番号iのカードが少なくとも1枚はi番目にくるような並べ替え方が存在しない条件をnについて求め、そのときのPnの値を答えよ。\n(3) Pnが最小となる最小のnの値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "n=3"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 10.0
                },
                {
                    "id": "math-math_a-probability-counts-level_D-2b3d8650-53be-49d9-84a8-b1e1994e50cf",
                    "serial_number": "数学A No.137",
                    "title": "カードの並べ替えと確率",
                    "instruction": "1からnまでの数字が書かれたカードが各1枚ずつ、合計n枚ある。これらを無作為に一列に並べるとき、どのカードもそのカードに書かれた数字と位置（左から1番目、2番目、…、n番目）が一致しないような並べ方をAnとする。n=4のとき、Anの値を求めよ。また、n=5のとき、Anの値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "9, 44"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_a-probability-counts-level_D-829928b3-6888-4916-85bc-ab1b659ede2d",
                    "serial_number": "数学A No.138",
                    "title": "硬貨の移動と確率の極限的推論",
                    "instruction": "数直線上の原点に駒がある。1枚の硬貨を投げ、表が出れば正の方向に1進み、裏が出れば負の方向に1進む。この試行をn回繰り返したとき、駒の位置が原点に戻る確率をp_nとする。\n(1) nが奇数のとき、p_nを求めよ。\n(2) n=2m (mは自然数) のとき、p_nをmを用いて表せ。\n(3) (2)のp_nについて、p_{2m+2} / p_{2m} をmの式で表したとき、その値が1/2以下となる最小の自然数mを求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "3"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 10.5
                }
            ]
        },
        {
            "title": "確率",
            "lessons": [
                {
                    "id": "math-math_a-probability-counts-level_D-b4e90839-89d4-4e96-8e32-7df89d5f6281",
                    "serial_number": "数学A No.139",
                    "title": "カードの引き直しと期待値",
                    "instruction": "1からnまでの数字が書かれたカードがそれぞれ1枚ずつ、合計n枚ある。この中から無作為に1枚引き、数字を確認して戻す試行をk回行う。得られたk個の数字の最大値をMとするとき、Mがnである確率をP(n, k)とする。\n(1) P(n, k)をnとkを用いて表せ。\n(2) kを固定したとき、lim_{n→∞} P(n, k) の値を求めよ。\n(3) 任意のnについて P(n, k) > 1/2 となる最小の自然数kをnを用いて表せ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "k ≧ log(2) / log(n/(n-1))"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_a-probability-counts-level_D-568b605f-cfcd-44de-9e7a-08d8887ef1f7",
                    "serial_number": "数学A No.241",
                    "subject_display": "数学A",
                    "title": "カードの引き直しと期待値",
                    "instruction": "1からnまでの数字が書かれたカードがそれぞれ1枚ずつ、合計n枚のカードがある。この中から1枚のカードを無作為に抜き出し、書かれた数字を確認して元に戻す。この試行をk回繰り返すとき、取り出されたk枚のカードの数字の最大値をXとする。Xの期待値E[X]をn, kを用いて表せ。ただし、n≧1, k≧1とする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "n - (n^k - 1) / (n^k * (n - 1) / n)"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.8
                }
            ]
        },
        {
            "title": "確率と漸化式",
            "lessons": [
                {
                    "id": "math-math_a-probability-counts-level_D-3d62965a-ab25-4978-9600-3ee9f66f438d",
                    "serial_number": "数学A No.205",
                    "subject_display": "数学A",
                    "title": "円周上の点における確率と漸化式",
                    "instruction": "円周上に等間隔に並んだn個の点P_1, P_2, ..., P_nがある。点P_1に動点Xがあり、1秒ごとに隣り合う点へそれぞれ確率1/2で移動する。点XがP_1から出発して、n秒後に再びP_1に位置している確率をp_nとする。このとき、p_nをnを用いて表せ。\nただし、n >= 2とする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "{1 + (1 - 2/n)^n} / 2"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.2
                }
            ]
        }
    ]
};