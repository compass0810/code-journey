window.practiceData = window.practiceData || {};
window.practiceData["math/math_c/representation/matrices/level_D"] = {
    "chapters": [
        {
            "title": "行列",
            "lessons": [
                {
                    "id": "math-math_c-representation-matrices-level_D-e3d2720b-fdfb-4ced-91fb-e32626f98589",
                    "title": "行列の累乗と存在条件",
                    "instruction": "2次正方行列A = ((a, 1), (1, a)) について、A^n の各成分がすべて正となるような実数aの範囲を求めよ。ただし、nは2以上の自然数とする。",
                    "answers": [
                        "a > 1"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学C No.88",
                    "subject_display": "数学C",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_c-representation-matrices-level_D-89f1bc5f-a868-45fa-bef3-5d2ac1559073",
                    "serial_number": "数学C No.89",
                    "title": "行列のべき乗とトレースの性質",
                    "instruction": "2次正方行列 A が A^2 - A + I = O (Iは単位行列) を満たしている。\n(1) A^n を A と I を用いて表すことによって、すべての自然数 n に対して A^n ≠ O であることを示せ。\n(2) A^n = a_n A + b_n I を満たす数列 {a_n}, {b_n} を用いるとき、行列 A^n のトレース(対角成分の和) tr(A^n) = 0 となるような n を、n ≡ p (mod q) の形で求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "n ≡ 2 (mod 3)"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学C",
                    "difficulty": 10.0
                },
                {
                    "id": "math-math_c-representation-matrices-level_D-6e8d6124-3ed8-490e-9f9d-a963a805f22d",
                    "serial_number": "数学C No.90",
                    "title": "行列のべき乗と不変部分空間",
                    "instruction": "2次正方行列 A = [[a, 1], [1, 0]] （ただし a は実数）について、A^n = [[x_n, y_n], [z_n, w_n]] とする。すべての自然数 n に対して、ベクトル v = (x, y) が A^n v = v を満たすような零ベクトル以外のベクトル v が存在するための a の値の範囲を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "-1 < a <= 2"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学C",
                    "difficulty": 10.5
                },
                {
                    "id": "math-math_c-representation-matrices-level_D-a8528052-5d4f-40d0-895b-b0bc552e0dfc",
                    "serial_number": "数学C No.163",
                    "subject_display": "数学C",
                    "title": "行列のべき乗と不変部分空間",
                    "instruction": "2次正方行列 A = [[a, b], [c, d]] (a, b, c, dは実数) が、A^2 = A を満たし、かつ行列 A が零行列でも単位行列でもないとする。このとき、トレース tr(A) = a + d の値として考えられるものをすべて答えよ。\nなお、行列 A の各成分は実数とし、A^2 = A を満たす条件の下で考えよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "1"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.5
                }
            ]
        },
        {
            "title": "行列",
            "lessons": [
                {
                    "id": "math-math_c-representation-matrices-level_D-e75a9d8c-adb6-40fb-91ff-80ff02920ca8",
                    "serial_number": "数学C No.91",
                    "title": "行列のべき乗とトレース",
                    "instruction": "2次正方行列A = (a, b; c, d)がA^3 = O を満たし、A ≠ O であるとする。このとき、A^2 ≠ O であることを示せ。また、A^2 = kA + mE （Eは単位行列）と表せるような定数k, mの組を求めよ。\nただし、Aの固有方程式を考える際、ケーリー・ハミルトンの定理を用いて論証すること。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "k=0, m=0"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学C",
                    "difficulty": 10.0
                },
                {
                    "id": "math-math_c-representation-matrices-level_D-502f96f7-3591-4e65-a859-314cdd90b8c1",
                    "serial_number": "数学C No.199",
                    "subject_display": "数学C",
                    "title": "行列の冪乗と恒等式",
                    "instruction": "2次正方行列Aが A^2 = A + I を満たしているとする（Iは単位行列）。このとき、ある自然数nに対して A^n = p_n A + q_n I と表される。この数列 {p_n}, {q_n} について、p_n を n を用いて表せ。ただし、Aはスカラー倍の単位行列ではないとする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "( ( (1+√5)/2 )^n - ( (1-√5)/2 )^n ) / √5"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.8
                }
            ]
        }
    ]
};