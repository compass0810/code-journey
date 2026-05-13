window.practiceData = window.practiceData || {};
window.practiceData["math/math_a/probability/sets/level_D"] = {
    "chapters": [
        {
            "title": "数学A：確率と集合",
            "lessons": [
                {
                    "id": "math-math_a-probability-sets-level_D-ad0de4dd-fcf0-45cd-a37e-b1f5fe113e8b",
                    "title": "集合と確率の境界値問題",
                    "instruction": "全体集合U = {1, 2, ..., n} の部分集合A, Bに対して、A ∩ B = φ かつ |A| = |B| = k であるとする。このとき、Uから選んだ2つの部分集合X, Yが X ⊂ A かつ Y ⊂ B を満たす確率をP(n, k)とする。P(n, k) = 1/144 となるような自然数の組(n, k)をすべて求め、そのときのnの値を合計せよ。",
                    "answers": [
                        "33"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学A No.154",
                    "subject_display": "数学A",
                    "difficulty": 10.0
                },
                {
                    "id": "math-math_a-probability-sets-level_D-5631bb2f-aadd-4009-8825-9107738734fe",
                    "serial_number": "数学A No.155",
                    "title": "集合と確率の包含関係",
                    "instruction": "全体集合U = {1, 2, ..., n} の部分集合 A, B を考える。n個の要素をそれぞれAまたはBまたはそのどちらにも属さない（A^cかつB^c）の3通りに振り分けるとき、以下の条件を満たす確率 P_n を求めよ。\n条件：A ⊂ B かつ A ≠ φ (空集合ではない)\n\n次に、P_n > 1/10 となる最小の自然数 n を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "n=5"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 10.0
                },
                {
                    "id": "math-math_a-probability-sets-level_D-190ba779-0352-4a6d-8623-3fd32a9427ba",
                    "serial_number": "数学A No.156",
                    "title": "集合と確率の境界値",
                    "instruction": "全体集合U = {1, 2, ..., n} の部分集合 A, B に対して、条件「A ∩ B = φ」を満たす組 (A, B) の総数を f(n) とする。また、A ∪ B = U を満たす組 (A, B) の総数を g(n) とする。n を自然数とするとき、f(n) / g(n) = 1/64 を満たす n の値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "6"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 10.0
                },
                {
                    "id": "math-math_a-probability-sets-level_D-2f8a0e9d-19c4-45a0-8969-bf3c7288620c",
                    "serial_number": "数学A No.245",
                    "subject_display": "数学A",
                    "title": "集合と確率の包含関係",
                    "instruction": "全体集合U = {1, 2, ..., n} の部分集合 A, B を考える。このとき、A ⊆ B となるような組 (A, B) の総数を S_n とする。また、A ∩ B = ∅ となるような組 (A, B) の総数を T_n とする。n = 3 のとき、S_n / T_n の値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "27/8"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.0
                }
            ]
        },
        {
            "title": "集合",
            "lessons": [
                {
                    "id": "math-math_a-probability-sets-level_D-6beba3b6-52f7-459a-85f3-312d5fa3a4ec",
                    "serial_number": "数学A No.157",
                    "title": "集合と確率の包含関係",
                    "instruction": "全体集合U = {1, 2, ..., n} の部分集合A, Bに対して、A ∩ B = ∅ かつ A ∪ B ≠ U を満たす組(A, B)の個数をN(n)とする。n ≧ 2 のとき、Uの任意の部分集合Xに対して、X ∩ A = ∅ かつ X ∩ B = ∅ を満たすような(A, B)の個数をf(X)とする。このとき、Σ[X⊂U] f(X) を n を用いて表せ。ただし、和はUのすべての部分集合Xについてとるものとする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "3^n"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 10.0
                }
            ]
        },
        {
            "title": "集合",
            "lessons": [
                {
                    "id": "math-math_a-probability-sets-level_D-3331210d-ed61-4555-b574-49efbd38f819",
                    "serial_number": "数学A No.158",
                    "title": "集合と確率の境界条件",
                    "instruction": "全体集合U = {1, 2, ..., n} の部分集合 A, B を考える。n個の要素からなる集合Uの部分集合の組 (A, B) は全部で 4^n 通り存在する。このうち、A ∩ B = ∅ を満たし、かつ A ∪ B ≠ U を満たすような組 (A, B) の個数を S_n とする。このとき、n個の要素からなる集合 U の部分集合の組 (A, B) を無作為に1つ選ぶとき、A ∩ B = ∅ かつ A ∪ B ≠ U となる確率 P_n を求め、その値が 1/4 未満となる最小の自然数 n を答えよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "3"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 10.0
                },
                {
                    "id": "math-math_a-probability-sets-level_D-f11e7d66-494b-4e5e-b5df-dd65e7f835e2",
                    "serial_number": "数学A No.209",
                    "subject_display": "数学A",
                    "title": "集合と確率の境界値問題",
                    "instruction": "全体集合U = {1, 2, ..., n} の部分集合A, Bに対して、A ∩ B = φ かつ A ∪ B ≠ φ を満たす組(A, B)の個数をP(n)とする。\n(1) P(n)をnを用いて表せ。\n(2) n個の要素からなる集合から、重複を許してm回選んでできる順列のうち、その選ばれた要素の集合をSとするとS = U を満たすようなものの個数をQ(m, n)とする。Q(m, n)を求めよ。\n(3) P(n) / 3^n がある値に収束するようにnを大きくするとき、その極限値を求めよ（※ただしこの問題では、(2)の知見を用い、n個の要素から集合を構成する際の包含排除の原理に関連する論理的考察を行うこととする）。\n\n問い: (3)の極限値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "0"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.0
                }
            ]
        }
    ]
};