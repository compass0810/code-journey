window.practiceData = window.practiceData || {};
window.practiceData["math/math_a/probability/basics/level_D"] = {
    "chapters": [
        {
            "title": "基礎",
            "lessons": [
                {
                    "id": "math-math_a-probability-basics-level_D-26ff0de1-a07b-4cdd-870c-8766c3905b4e",
                    "title": "確率と隣接3項間漸化式の応用",
                    "instruction": "1個のさいころを投げ、出た目に応じて数直線上の点Pを動かす。最初、点Pは原点0にある。さいころを投げて1または2の目が出たら正の方向に1進み、3以上の目が出たら負の方向に1進む。この試行をn回繰り返した後に、点Pが原点0に戻っている確率をp_nとする。p_0=1, p_1=0として、p_nをnを用いて表せ。",
                    "answers": [
                        "p_n = (1+(-1/2)^n)/3 (ただしnが偶数のとき) / 0 (ただしnが奇数のとき)"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学A No.110",
                    "subject_display": "数学A",
                    "difficulty": 10.2
                },
                {
                    "id": "math-math_a-probability-basics-level_D-f455c95d-a82c-4ae0-a606-c58334ef6340",
                    "serial_number": "数学A No.111",
                    "title": "赤玉と白玉の入れ替え試行",
                    "instruction": "赤玉3個、白玉2個が入った袋がある。この袋から同時に2個の玉を取り出し、その色が異なるときは取り出した赤玉を白玉に、白玉を赤玉に置き換えて袋に戻す。色が同じときは何もせず袋に戻す。この試行をn回繰り返した後の袋の中の赤玉の個数をXnとする。X0=3であるとき、Xnの期待値E(Xn)をnを用いて表せ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "3-(1/2)^n"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_a-probability-basics-level_D-d461f988-91d1-41cd-90f2-ccbf124f466f",
                    "serial_number": "数学A No.112",
                    "title": "赤玉と白玉の入れ替え試行",
                    "instruction": "袋の中に赤玉が2個、白玉が1個入っている。以下の操作を繰り返し行う。\n「袋から玉を1個取り出し、その玉の色を確認してから袋に戻す。このとき、取り出した玉が赤ならば、別の袋から赤玉1個を追加し、白ならば、袋の中の赤玉を1個取り出して捨てる（ただし、袋の中に赤玉がない状態で白玉が出た場合は、何もせず赤玉数は0のままとする）。」\n最初、袋の中には赤玉が2個、白玉が1個入っているとする。n回操作を行った後に、袋の中の赤玉がちょうど2個である確率をp_nとする。p_1, p_2を求め、n→∞のときの極限値pを求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "p_1=2/3, p_2=5/9, p=1/2"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_a-probability-basics-level_D-621b89c8-1262-4127-98a3-4f0c10aae257",
                    "serial_number": "数学A No.237",
                    "subject_display": "数学A",
                    "title": "硬貨の移動と確率の極限",
                    "instruction": "数直線上の原点に駒がある。1枚の硬貨を投げ、表が出れば正方向に1進み、裏が出れば負方向に1進む操作をn回繰り返す。n回終了後に駒が原点にある確率をp_nとする。nが偶数のとき、p_nをnを用いて表し、n→∞におけるp_nの挙動を考察した上で、n回目までに一度も原点に戻らない確率をq_nとするとき、q_nをnを用いて表せ（n=2kとする）。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "p_2k = (2k)! / (k!k! * 2^2k), q_2k = 1 / (2k-1) * (2k)! / (k!k! * 2^2k)"
                    ],
                    "matchType": "exact",
                    "difficulty": 10.5
                }
            ]
        },
        {
            "title": "基礎",
            "lessons": [
                {
                    "id": "math-math_a-probability-basics-level_D-6e27ef0a-72bc-469d-8b3c-270ff90188c8",
                    "serial_number": "数学A No.113",
                    "title": "硬貨の移動と確率の極限的推論",
                    "instruction": "数直線上の原点に駒がある。コインを投げて表が出れば正の方向に1進み、裏が出れば負の方向に1進む試行をn回繰り返す。n回終了後に駒が位置0にある確率をP_nとする。ただし、nが奇数のときP_n = 0である。また、n=2m（mは正の整数）のとき、駒が位置0に一度も戻ることなく終了する確率をQ_{2m}とする。このとき、P_{2m}をmを用いて表し、Q_{2m} = 1/(m+1) * P_{2m} が成立することを示せ。その上で、P_{2m}を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "(2m)! / (4^m * (m!)^2)"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 10.5
                },
                {
                    "id": "math-math_a-probability-basics-level_D-64f45472-bf28-4a7c-92b4-2b13adf3767b",
                    "serial_number": "数学A No.201",
                    "subject_display": "数学A",
                    "title": "カードの引き直しと条件付き確率",
                    "instruction": "赤玉が3個、白玉が2個入った袋がある。この袋から玉を1個取り出し、色を確認して袋に戻す試行を3回行う。ただし、1回目または2回目に白玉が出た場合、その直後の試行においてのみ、袋の中身を「赤玉4個、白玉1個」に入れ替えてから玉を取り出すものとする。3回目に赤玉が出る確率を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "179/250"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.5
                }
            ]
        },
        {
            "title": "確率",
            "lessons": [
                {
                    "id": "math-math_a-probability-basics-level_D-a022b918-5ea1-410f-b513-2676fad95115",
                    "serial_number": "数学A No.114",
                    "title": "硬貨の移動と確率の極限",
                    "instruction": "数直線上の原点に駒がある。1枚の硬貨を投げ、表が出れば正の方向に1進み、裏が出れば負の方向に1進む試行をn回繰り返す。n回終了後に駒が原点に戻る確率をP(n)とする。\n(1) P(2n)をnを用いて表せ。\n(2) nを大きくしたとき、P(2n)はどのような値に近づくか。また、その近似値として、nが十分に大きいときのP(2n)を階乗を用いずにnの式で表せ（ウォリスの公式等の評価を用いてよい）。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "P(2n) = (2n)! / (4^n * (n!)^2), 1/sqrt(n*pi)"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学A",
                    "difficulty": 10.5
                }
            ]
        }
    ]
};