window.practiceData = window.practiceData || {};
window.practiceData["math/math_1/data_analysis/correlation/level_D"] = {
    "chapters": [
        {
            "title": "データの分析",
            "lessons": [
                {
                    "id": "math-math_1-data_analysis-correlation-level_D-fd6bf6ea-d5a6-4258-baf8-bdcaa2caf871",
                    "title": "相関係数の最大化と変数の範囲",
                    "instruction": "5個のデータ (x_1, y_1), ..., (x_5, y_5) があり、x_i は 1, 2, 3, 4, 5 である。また、y_i = a・x_i + b_i (i=1, ..., 5) で表され、ここで a > 0 とする。各 y_i に対して、分散 s_y^2 が 1 となり、かつ x と y の共分散 s_xy が 1 となるように b_1, ..., b_5 をとるとき、a がとりうる値の範囲を求めよ。\n（ヒント：共分散 s_xy と相関係数 r の関係および、分散の定義式を利用すること）",
                    "answers": [
                        "0 < a <= 1/sqrt(2)"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学I No.49",
                    "subject_display": "数学I",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_1-data_analysis-correlation-level_D-1f7257de-1105-4159-92e3-3d4ee61aca0a",
                    "serial_number": "数学I No.50",
                    "title": "相関係数の変域と定数の条件",
                    "instruction": "n個のデータ (x_i, y_i) (i=1, 2, ..., n) があり、x_iの平均をx_bar、y_iの平均をy_barとする。各データの偏差を u_i = x_i - x_bar, v_i = y_i - y_bar とおくと、Σu_i^2 = 10, Σv_i^2 = 40, Σu_iv_i = 12 が成り立っている。\nいま、新しいデータ (X_i, Y_i) を X_i = x_i, Y_i = a*x_i + y_i (aは実数) と定義する。\nデータ (X_i, Y_i) の相関係数を r(a) とするとき、r(a) = 0 となるようなaの値を求めよ。また、r(a) の値が定義されるためのaの条件を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "a = -3/5, a > -2/5"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_1-data_analysis-correlation-level_D-0298c318-0409-43bc-9893-9fcf7a8bb2ea",
                    "serial_number": "数学I No.51",
                    "title": "相関係数の最大化と変数の制約",
                    "instruction": "n個のデータ(x_i, y_i) (i=1, 2, ..., n)があり、それぞれの平均は0、分散は1であるとする。また、相関係数をrとする。ここで、新たな変数z_i = a*x_i + y_i (aは実数)を定義し、z_iの分散をV_zとする。V_zが最小となるようなaの値を用いて、相関係数rをV_zの最小値を用いて表せ。その上で、n=5、Σx_i*y_i = 3のとき、このデータの相関係数rを求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "3/5"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.6
                },
                {
                    "id": "math-math_1-data_analysis-correlation-level_D-10ee6f6c-e032-4bb7-89bf-1619177fdd47",
                    "serial_number": "数学I No.52",
                    "title": "相関係数と変数の線形変換",
                    "instruction": "あるデータの組(x_i, y_i) (i=1, 2, ..., n) について、xの平均をx_bar、yの平均をy_bar、分散をs_x^2, s_y^2、共分散をs_{xy}とする。また、相関係数をrとする。ここで、新たな変数 u_i = ax_i + b, v_i = cy_i + d (a, c ≠ 0) を導入する。以下の条件を満たすとき、相関係数rの値を求めよ。\n条件1: u_i と v_i の相関係数 r_{uv} = -r\n条件2: a と c が異符号であるならば、ある実数 k > 0 を用いて |a| = k, |c| = 2k と表される\n条件3: a と c が同符号であるならば、r_{uv} = r となる\nなお、a, c は0でない定数とする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "-1"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.2
                },
                {
                    "id": "math-math_1-data_analysis-correlation-level_D-501da7bb-66b2-4da5-bbfc-967beeff08d2",
                    "serial_number": "数学I No.312",
                    "subject_display": "数学I",
                    "title": "相関係数の最大化と変数の制約",
                    "instruction": "n個のデータ(x_i, y_i) (i=1, 2, ..., n)があり、それぞれの平均は0、分散はともに1であるとする。また、すべてのiに対して y_i = ax_i + b となるような定数a, bが存在しないものとする。このとき、相関係数r = (1/n)Σx_i y_i について、次の問いに答えよ。\n(1) 任意のデータに対して、|r| < 1 が成り立つことを証明せよ。\n(2) x_i + y_i = c (cは定数) という制約条件があるとき、rのとりうる最小値を求めよ。ただし、データの個数nは十分に大きく、Σx_i^2 = n, Σy_i^2 = n を満たすとする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "-1"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.6
                },
                {
                    "id": "math-math_1-data_analysis-correlation-level_D-f7830c9d-3d9a-4270-b18b-1979f56898f8",
                    "serial_number": "数学I No.361",
                    "subject_display": "数学I",
                    "title": "相関係数と変量変換の不等式",
                    "instruction": "n個のデータ x1, x2, ..., xn (n ≧ 3) があり、平均値は 0、分散は 1 である。また、新たなデータ yi = axi + b (i=1, ..., n) を考える。ここで、xとyの相関係数が 1 であり、yの分散が 4 であるとき、bの値を求め、さらに a > 0 の条件下で、すべての i について |yi| ≦ 1 が成り立つための a の範囲を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "b=0, 0 < a ≦ 1/max(|x1|, ..., |xn|)"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.4
                }
            ]
        },
        {
            "title": "データ分析",
            "lessons": [
                {
                    "id": "math-math_1-data_analysis-correlation-level_D-ef14c7ef-e380-46e9-b929-219a7b57b1f0",
                    "serial_number": "数学I No.53",
                    "title": "相関係数の変域と定数の決定",
                    "instruction": "n個のデータ (x_1, y_1), (x_2, y_2), ..., (x_n, y_n) がある。各データの偏差を u_i = x_i - x_mean, v_i = y_i - y_mean (x_mean, y_meanは平均値) とし、S_x^2 = Σu_i^2, S_y^2 = Σv_i^2, S_xy = Σu_i v_i とする。n=5であり、u_i^2 = 1, v_i^2 = 1 (i=1, 2, ..., 5) が成り立っているとき、相関係数 r = S_xy / √(S_x^2 S_y^2) がとりうる値の範囲を求めよ。ただし、各データにおいて x_i ≠ x_mean かつ y_i ≠ y_mean であるとする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "-1 < r < 1"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.5
                }
            ]
        },
        {
            "title": "データの分析（相関関係）",
            "lessons": [
                {
                    "id": "math-math_1-data_analysis-correlation-level_D-5ad104ee-16dc-4ff7-be1f-ad1bb197bd8d",
                    "serial_number": "数学I No.54",
                    "title": "相関係数と変数の線形変換",
                    "instruction": "2つの変量x, yのデータがn個あり、それぞれの平均値をx_bar, y_bar、分散をs_x^2, s_y^2、共分散をs_{xy}とする。ここで、新しい変数u, vをu = ax + b, v = cy + d (a > 0, c < 0) と定義する。\n(1) uとvの相関係数r_{uv}を、xとyの相関係数r_{xy}を用いて表せ。\n(2) xとyのデータに対し、分散s_x^2 = 4, s_y^2 = 9, 共分散s_{xy} = -4 が与えられている。このとき、a=1/2, c=-1/3 とすると、相関係数r_{uv}の値はいくらになるか。その数値を答えよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "-1"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.2
                }
            ]
        },
        {
            "title": "相関関係",
            "lessons": [
                {
                    "id": "math-math_1-data_analysis-correlation-level_D-875616a1-893a-41dd-bc3e-79244f376a09",
                    "serial_number": "数学I No.55",
                    "title": "相関係数の制約と変数の範囲",
                    "instruction": "n個のデータ(x_i, y_i) (i=1, 2, ..., n)があり、各変数の平均は0、分散は1であるとする。すなわち、Σx_i = Σy_i = 0 かつ (1/n)Σx_i^2 = (1/n)Σy_i^2 = 1 を満たす。このとき、相関係数 r = (1/n)Σx_i y_i が |r| < 1 であるとする。ここで、新たな変数 z_i = x_i + ay_i (aは実数の定数) を定義する。z_i の分散を V_z とするとき、V_z が最小となるような a の値を用い、そのときの最小値 V_{z,min} を r を用いて表せ。また、V_{z,min} = 1/2 となるような r の値をすべて求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "r = 1/sqrt(2), -1/sqrt(2)"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.7
                }
            ]
        }
    ]
};