window.practiceData = window.practiceData || {};
window.practiceData["math/math_b/sequences/induction/level_D"] = {
    "chapters": [
        {
            "title": "数列（数学的帰納法）",
            "lessons": [
                {
                    "id": "math-math_b-sequences-induction-level_D-2fd8ad70-5cd1-4e08-bf8c-7a3c234749f8",
                    "title": "漸化式と数学的帰納法による不等式の証明",
                    "instruction": "数列{a_n}が a_1 = 1, a_{n+1} = a_n + 1/a_n (n=1, 2, ...) で定義されるとき、すべての自然数nに対して、√{2n} < a_n < √(2n) + 1/(2√(2n)) が成り立つことを数学的帰納法を用いて示せ。また、この不等式を用いて、lim_{n→∞} a_n/√(2n) の値を求めよ。",
                    "answers": [
                        "1"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学B No.36",
                    "subject_display": "数学B",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_b-sequences-induction-level_D-0244326f-0ad4-4415-bb90-8aece322bdd9",
                    "serial_number": "数学B No.37",
                    "title": "数列の漸化式と数学的帰納法",
                    "instruction": "数列{a_n}が a_1 = 1, a_{n+1} = a_n + 2n(a_n)^2 (n=1, 2, 3, ...) を満たすとき、すべての自然数nに対して a_n < 1/n が成り立つことを数学的帰納法を用いて証明せよ。また、この不等式を利用して、無限級数 Σ_{n=1}^{∞} a_n が収束することを示せ。このとき、Σ_{n=1}^{∞} a_n の値がとりうる範囲を以下の形式で答えよ。（※n=1から無限大までの和をSとする）",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "0 < S < 1"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.7
                },
                {
                    "id": "math-math_b-sequences-induction-level_D-c9900585-e073-4363-949e-b532872b5fff",
                    "serial_number": "数学B No.38",
                    "title": "漸化式と数学的帰納法による不等式の証明",
                    "instruction": "数列{a_n}が a_1 = 1, a_{n+1} = a_n + 1/a_n (n=1, 2, ...) を満たすとき、すべての自然数nに対して 2√(n-1) < a_n < 2√n が成り立つことを数学的帰納法を用いて示せ。また、この不等式を利用して、lim(n→∞) a_n/√n の値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "2"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 9.9
                }
            ]
        },
        {
            "title": "数学的帰納法",
            "lessons": [
                {
                    "id": "math-math_b-sequences-induction-level_D-2d8217a8-8a89-49f1-a942-6273919d7d35",
                    "serial_number": "数学B No.39",
                    "title": "漸化式と数学的帰納法による不等式の証明",
                    "instruction": "数列{a_n}が a_1 = 1, a_{n+1} = a_n + 1/a_n (n=1, 2, ...) で定義される。すべての自然数nに対して、不等式 2√(n-1) < a_n < 2√n が成り立つことを数学的帰納法を用いて証明せよ。また、この不等式を利用して、lim_{n→∞} a_n/√n の値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "2"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 10.1
                },
                {
                    "id": "math-math_b-sequences-induction-level_D-679ea5a9-4672-40d7-91eb-a30364a0e97b",
                    "serial_number": "数学B No.133",
                    "subject_display": "数学B",
                    "title": "数列の漸化式と数学的帰納法",
                    "instruction": "数列{a_n}が a_1 = 1, a_{n+1} = a_n + 1/a_n (n=1, 2, 3, ...) で定義されるとき、すべての自然数nに対して 2*sqrt(n) < a_n < 2*sqrt(n) + 1/(8*sqrt(n)) が成り立つことを数学的帰納法を用いて示せ。また、この不等式を用いて、n -> ∞ のときの a_n / sqrt(n) の極限値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "2"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.3
                }
            ]
        },
        {
            "title": "数学B 数列（数学的帰納法）",
            "lessons": [
                {
                    "id": "math-math_b-sequences-induction-level_D-b66adcda-37d3-44a3-90b9-d19e9e23ab08",
                    "serial_number": "数学B No.40",
                    "title": "漸化式と帰納的論証",
                    "instruction": "数列{a_n}が a_1 = 1, a_{n+1} = a_n + 1/a_n (n=1, 2, 3, ...) で定義される。すべての自然数nに対して、不等式 2n < a_n^2 < 2n + log(n) + 1 が成り立つことを数学的帰納法を用いて示せ。また、この不等式を用いて極限値 lim_{n→∞} (a_n / sqrt(n)) を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "sqrt(2)"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学B",
                    "difficulty": 10.5
                }
            ]
        },
        {
            "title": "数学的帰納法",
            "lessons": [
                {
                    "id": "math-math_b-sequences-induction-level_D-a036e00e-eb74-4e7c-bb6e-828011032ae1",
                    "serial_number": "数学B No.161",
                    "subject_display": "数学B",
                    "title": "数列の漸化式と数学的帰納法",
                    "instruction": "数列{a_n}が a_1 = 1, a_{n+1} = a_n + 2n(a_n)^2 (n=1, 2, 3, ...) を満たすとき、すべての自然数nに対して a_n < 1/n が成り立つような定数kの範囲を求めよ、という問いを考える。このとき、a_n = 1/(n+c) という形式にはならないが、不等式 1/(n+k) < a_n < 1/n が成り立つような定数kの最小値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "1"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.7
                }
            ]
        }
    ]
};