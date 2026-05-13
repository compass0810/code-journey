window.practiceData = window.practiceData || {};
window.practiceData["math/math_a/probability/various/level_D"] = {
    "chapters": [
        {
            "title": "確率",
            "lessons": [
                {
                    "id": "math-math_a-probability-various-level_D-dd44ea4f-d0a8-40f3-9c0c-346fa06ad788",
                    "title": "確率と漸化式による状態推移",
                    "instruction": "座標平面上の原点Oを出発し、1秒ごとに以下のルールで移動する点Pがある。\n「点Pの現在の座標を(x,y)とするとき、確率1/2で(x+1,y)へ、確率1/2で(x,y+1)へ移動する。」\nこのとき、n秒後の点Pの座標を(Xn, Yn)とする。Xn+Yn=nであることは自明である。n秒後の点Pが直線 y = x + k (kは整数) 上に存在しない確率をPnとする。n=4のとき、Pnが最小となる整数kの値と、そのときのPnの値を求めよ。ただし、nが偶数の場合のみを考えることとする。",
                    "answers": [
                        "k=0, P4=3/8"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学A No.173",
                    "subject_display": "数学A",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_a-probability-various-level_D-a108da69-80ed-422f-864b-aae5a11c56d5",
                    "serial_number": "数学A No.174",
                    "title": "カードの引き直しと条件付き確率",
                    "instruction": "1からnまでの数字が書かれたカードがそれぞれ1枚ずつ、合計n枚ある。この中から1枚を引き、数字を確認して元に戻す。この試行を独立に2回行うとき、1回目に出た数字をX、2回目に出た数字をYとする。いま、条件「X < Y」が満たされる事象をA、条件「XとYの少なくとも一方が素数である」という事象をBとする。n = 5のとき、条件付き確率P_A(B)を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "3/5"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 9.6
                },
                {
                    "id": "math-math_a-probability-various-level_D-df9131c8-6dd4-4017-bc8e-582de2638345",
                    "serial_number": "数学A No.175",
                    "title": "確率と漸化式の極限",
                    "instruction": "1辺の長さが1の正三角形の頂点をA, B, Cとする。動点Pは最初頂点Aにあり、1秒ごとに隣接する2頂点のいずれかに等確率で移動する。n秒後に点Pが頂点Aにある確率をp_nとする。このとき、p_nをnを用いて表し、n→∞のときの極限値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "(1 + 2(-1/2)^n)/3, 1/3"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_a-probability-various-level_D-ab1743be-7e48-43a1-902c-b9f375a46e19",
                    "serial_number": "数学A No.176",
                    "title": "赤玉と白玉の確率的推移",
                    "instruction": "袋の中に赤玉1個と白玉1個が入っている。この袋から1個の玉を取り出し、その色を確認してから袋に戻し、代わりに赤玉1個を袋に加える試行を繰り返す。n回目の試行終了後の袋の中の赤玉の数をR_n、白玉の数をW_nとし、その総数をS_n = R_n + W_nとする。n回目の試行で赤玉を取り出す確率をp_nとするとき、p_nをnを用いて表し、lim(n→∞) p_n の値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "1"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 10.0
                },
                {
                    "id": "math-math_a-probability-various-level_D-e6cdb0d8-d6f5-4e21-b8ee-8503c7df372f",
                    "serial_number": "数学A No.249",
                    "subject_display": "数学A",
                    "title": "確率と漸化式の極限",
                    "instruction": "1辺の長さが1である正六角形ABCDEFの頂点Aに動点Pがある。サイコロを振って出た目に応じて、以下のルールでPを移動させる。\n1. 1, 2の目が出たとき、反時計回りに隣の頂点へ移動する。\n2. 3, 4の目が出たとき、時計回りに隣の頂点へ移動する。\n3. 5, 6の目が出たとき、現在の頂点に留まる。\nn回移動した後のPが頂点Aにある確率をp_nとする。p_0 = 1とし、n→∞におけるp_nの値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "1/6"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.2
                }
            ]
        },
        {
            "title": "数学A：確率",
            "lessons": [
                {
                    "id": "math-math_a-probability-various-level_D-2c716ab2-1672-40e4-8ef7-fcda165366b1",
                    "serial_number": "数学A No.177",
                    "title": "カードの引き直しと条件付き確率",
                    "instruction": "1からnまでの番号が書かれたカードがそれぞれ1枚ずつ、計n枚ある。この中から1枚を引き、番号を確認して戻す操作を2回行う。1回目に出た番号をX、2回目に出た番号をYとする。いま、X < Y となる確率をP_nとする。さらに、この操作を独立にm回行い、そのうちX < Y となる回数をKとする。Kが最大値をとる確率が、どのm（m≧1）に対しても一意に定まるようなnの範囲を求めよ。\n（ただし、nは2以上の整数とする）",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "n=2"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 10.4
                },
                {
                    "id": "math-math_a-probability-various-level_D-f9328d83-6e41-47d5-97a3-65ed819f2c43",
                    "serial_number": "数学A No.213",
                    "subject_display": "数学A",
                    "title": "確率と漸化式の極限",
                    "instruction": "1辺の長さが1である正方形の4つの頂点を反時計回りにA, B, C, Dとする。動点Pは最初頂点Aにあり、1回の試行ごとに、Pは隣接する2つの頂点にそれぞれ確率1/3で移動し、その場（現在の頂点）に確率1/3で留まるものとする。n回の試行後にPが頂点Aにある確率をp_nとする。p_0=1とし、n→∞のときのp_nの極限値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "1/4"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.6
                }
            ]
        }
    ]
};