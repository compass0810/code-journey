window.practiceData = window.practiceData || {};
window.practiceData["math/math_c/representation/data/level_D"] = {
    "chapters": [
        {
            "title": "データの分析",
            "lessons": [
                {
                    "id": "math-math_c-representation-data-level_D-4c833a90-2f03-42bd-bb1e-d9d12ec94a68",
                    "title": "散布図と相関係数の変域",
                    "instruction": "n個のデータ (x_1, y_1), (x_2, y_2), ..., (x_n, y_n) がある。各データの平均値は共に0であり、分散は共に1であるとする。また、x_i + y_i = k_i (i=1, 2, ..., n) とおき、すべての k_i について |k_i| <= 1 が成り立つとする。このとき、xとyの相関係数 r のとりうる値の範囲を求めよ。",
                    "answers": [
                        "-1 <= r <= 1/2"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学C No.74",
                    "subject_display": "数学C",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_c-representation-data-level_D-31da0674-6101-42e9-a6ac-24e226315bea",
                    "serial_number": "数学C No.75",
                    "title": "分散の最小値と定数の決定",
                    "instruction": "n個のデータ x_1, x_2, ..., x_n (n≧3) があり、すべてのデータの平均値は 0、分散は 1 である。このとき、新たなデータ y_i = x_i + a (i=1, ..., n) を考える。y_1, y_2, ..., y_n の平均値を m、分散を s^2 とするとき、s^2 が a の値によらず 1 であることを示せ。また、n個のデータ z_i = c * x_i + d (c > 0) の分散が 4 であり、かつ、すべてのデータ z_i が閉区間 [-2, 2] に含まれるとき、c の値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "c=2"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学C",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_c-representation-data-level_D-fc80e5cc-acc3-4eb3-8d1b-5d36172f2ac7",
                    "serial_number": "数学C No.76",
                    "title": "分散の最小値と定数の決定",
                    "instruction": "n個のデータ x_1, x_2, ..., x_n (n≧3) があり、すべてのデータの平均値は 0 で、分散は 1 であるとする。このとき、y_i = x_i + a (i=1, ..., n) とおくと、y_1, ..., y_n の分散は 1 である。ここで、新たなデータ z_i = x_i + c*x_i^2 (cは定数) を考える。すべての i について z_i = 0 となるようなデータの組 (x_1, ..., x_n) が存在し、かつこのときデータ z_1, ..., z_n の分散が 0 となるような c の値は c = 0 のみであるという条件のもとで、データ群の積率を考慮し、Σx_i^3 = 0 かつ Σx_i^4 = n*k を満たすとき、n=4 において Σz_i^2 が最小値をとるための c の値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "c=0"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学C",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_c-representation-data-level_D-58f07a4d-3930-4ee9-a84c-a6eff030c2f6",
                    "serial_number": "数学C No.77",
                    "title": "分散の最小値と定数の決定",
                    "instruction": "n個のデータ x_1, x_2, ..., x_n (n≧3) があり、すべてのデータの平均値は 0、分散は 1 であるとする。このとき、a を実数として、新たなデータ y_i = x_i + a (i=1, ..., n) を考える。y_1^2 + y_2^2 + ... + y_n^2 の値が最小となるときの a の値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "0"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学C",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_c-representation-data-level_D-02b89090-5856-41b6-997e-5260a65a8108",
                    "serial_number": "数学C No.159",
                    "subject_display": "数学C",
                    "title": "分散の最小値と相関係数",
                    "instruction": "n個のデータx_1, x_2, ..., x_nがあり、その平均をx_bar、分散をs^2とする。すべてのデータに対してy_i = x_i - x_bar (i=1, ..., n) とおき、y_1, ..., y_nの平均を0、分散をs^2とする。ここで、新たなデータz_i = a*x_i + b (a > 0) を導入する。xとzの相関係数が1であるとき、y_iとz_iの共分散をsを用いて表せ。また、z_1^2 + z_2^2 + ... + z_n^2 が最小値をとるような a, b を、x_bar, s^2 を用いて表せ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "a*s^2, a=0, b=0"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.2
                },
                {
                    "id": "math-math_c-representation-data-level_D-da023198-a1d9-4383-9ebd-8bda41e77ca0",
                    "serial_number": "数学C No.195",
                    "subject_display": "数学C",
                    "title": "分散の最小値と相関係数",
                    "instruction": "n個のデータ x1, x2, ..., xn (n ≧ 2) があり、その平均値は 0、分散は 1 であるとする。また、別のデータ y1, y2, ..., yn が y_i = ax_i + b (i=1, ..., n) で与えられており、yの平均値は 0、分散は 4 であるとする。このとき、データ x と y の相関係数 r を求めよ。また、データ z_i = x_i + y_i について、z_i^2 の平均値が最小となるときの a, b の値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "r=1, a=2, b=0 または r=-1, a=-2, b=0"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.2
                }
            ]
        }
    ]
};