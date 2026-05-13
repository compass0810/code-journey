window.practiceData = window.practiceData || {};
window.practiceData["math/math_1/data_analysis/application/level_D"] = {
    "chapters": [
        {
            "title": "データの分析",
            "lessons": [
                {
                    "id": "math-math_1-data_analysis-application-level_D-14a2334b-a5c7-4e67-8667-14683a1ea504",
                    "title": "データ分析と相関係数の範囲",
                    "instruction": "n個のデータ(x_i, y_i) (i=1, 2, ..., n)があり、各データの平均値は0、分散はともに1であるとする。すなわち、Σx_i = Σy_i = 0 かつ (1/n)Σx_i^2 = (1/n)Σy_i^2 = 1 を満たす。このとき、相関係数 r = (1/n)Σx_i y_i について、以下の問いに答えよ。\n新たなデータ z_i = x_i + a*y_i (aは実数) を考える。z_i の分散が 0 以上であるという条件から、a の値によらず成立する r のとりうる値の範囲を求めよ。",
                    "answers": [
                        "-1 <= r <= 1"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学I No.21",
                    "subject_display": "数学I",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_1-data_analysis-application-level_D-d0b65272-2881-4b00-bb3a-dc57702c2fba",
                    "serial_number": "数学I No.22",
                    "title": "データ分析と相関係数の最大値",
                    "instruction": "n個のデータ (x1, y1), (x2, y2), ..., (xn, yn) があり、各データについて xi > 0, yi > 0 を満たしている。また、Σxi = Σyi = n かつ Σxi^2 = Σyi^2 = S (Sは定数) が成り立っている。このとき、xとyの相関係数 r を S を用いて表せ。また、このデータがどのような配置にあるとき、r は最大値をとるか論ぜよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "r = (S-n)/ (S-n) = 1 (ただし xi = yi のとき)"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.8
                },
                {
                    "id": "math-math_1-data_analysis-application-level_D-0afe98f5-ccca-40f1-af8d-673669d7207a",
                    "serial_number": "数学I No.23",
                    "title": "データ分析と相関係数の範囲",
                    "instruction": "n個のデータx_1, x_2, ..., x_n（n≧3）があり、その平均値をx_aveとする。各データの偏差をd_i = x_i - x_aveとし、分散をs^2とする。また、別のデータy_i = ax_i + b (a < 0) を考える。このとき、xとyの相関係数rは常に-1であることを示せ。また、n=3のとき、x_1=0, x_2=1, x_3=xとし、y_1=3, y_2=1, y_3=yとすると、xとyの相関係数が-1となるようなyをxの式で表せ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "y = -2x + 3"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_1-data_analysis-application-level_D-cffd307d-d4b1-4974-8af6-0af34c41aa58",
                    "serial_number": "数学I No.24",
                    "title": "データ分析と相関係数の範囲",
                    "instruction": "n個のデータ(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)について、それぞれの平均をx_bar, y_bar、分散をs_x^2, s_y^2、共分散をs_xyとする。これらを用いた相関係数r = s_xy / (s_x * s_y)について考える。\nすべてのデータについて y_i = a * x_i + b (a, bは定数) が成り立つとき、相関係数rの値として取りうるすべての値を求めよ。\nなお、s_x > 0 とする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "a > 0 のとき 1, a < 0 のとき -1"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_1-data_analysis-application-level_D-7989d577-7596-4675-88f6-0960198be775",
                    "serial_number": "数学I No.25",
                    "title": "データ分析と相関係数の評価",
                    "instruction": "n個のデータ(x_1, y_1), (x_2, y_2), ..., (x_n, y_n) がある。各データの平均をそれぞれx_avg, y_avgとし、分散をV_x, V_y、共分散をS_{xy}とする。すべてのi (1 ≦ i ≦ n) について、y_i = a x_i + b が成り立つとき、相関係数rをaの符号を用いて表し、また、x_iがすべて等しくないという条件の下で、rの値として取りうる値をすべて求めよ。\n\nヒント：相関係数 r = S_{xy} / (√V_x * √V_y)",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "a > 0のとき1, a < 0のとき-1"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.6
                },
                {
                    "id": "math-math_1-data_analysis-application-level_D-9f1142fd-7055-49b3-a29f-d76cca7810ea",
                    "serial_number": "数学I No.26",
                    "title": "データ分析と相関係数の評価",
                    "instruction": "n個のデータ(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)がある。各データの平均をそれぞれx_bar, y_barとし、分散をs_x^2, s_y^2、共分散をs_{xy}とする。また、全てのiについてy_i = ax_i + b (a < 0) が成り立っているとする。このとき、xとyの相関係数rをaとbを用いて表せ。さらに、n=5、データの平均がx_bar = 2、y_bar = 3であり、Σ(x_i - x_bar)^2 = 10、Σ(x_i - x_bar)(y_i - y_bar) = -20であるとき、定数aおよびbの値を求めよ。\n※答えは順に、rの値、aの値、bの値の順で記述せよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "-1, -2, 7"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.6
                },
                {
                    "id": "math-math_1-data_analysis-application-level_D-60ee3774-c899-4739-a9e1-07dfff04bbb9",
                    "serial_number": "数学I No.27",
                    "title": "データ分析と相関係数の範囲",
                    "instruction": "n個のデータ(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)において、それぞれの平均値をx¯, y¯、分散をsx^2, sy^2、共分散をsxyとする。各データについて、x_i' = ax_i + b (a > 0), y_i' = cy_i + d (c < 0) と変換した新しいデータ群の相関係数をr'とする。変換前の相関係数がrであるとき、r'をrを用いて表せ。また、rがとりうる値の範囲が-1 < r < 1であるとき、r'のとりうる値の範囲を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "-1 < r' < 1"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_1-data_analysis-application-level_D-0f1d7bf6-d451-472b-852a-93bbc6021348",
                    "serial_number": "数学I No.308",
                    "subject_display": "数学I",
                    "title": "データ分析と相関係数の範囲",
                    "instruction": "n個のデータ(x_1, y_1), (x_2, y_2), ..., (x_n, y_n) がある。各変数の平均を0、分散をそれぞれs_x^2, s_y^2とする。ここで、すべてのiについてy_i = ax_i + b (a≠0) が成り立つとき、xとyの相関係数rをaを用いて表せ。また、このデータにおいて、xとyの共分散s_xyがs_x^2と等しくなるためのaの値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "a > 0のときr=1, a < 0のときr=-1, a=1"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_1-data_analysis-application-level_D-75781ff2-4d69-404a-937f-528412821b7c",
                    "serial_number": "数学I No.357",
                    "subject_display": "数学I",
                    "title": "データ分析と相関係数の範囲",
                    "instruction": "n個のデータ(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)において、x_i, y_i はそれぞれ平均が0、分散が1であるとする。このとき、相関係数rが r = (1/n) * Σ(x_i * y_i) で定義されるとき、Σ(x_i - y_i)^2 を r を用いて表せ。また、n個のデータについて、ある定数 a に対してすべての i について y_i = a * x_i + b となるような状況を考えたとき、相関係数 r がとりうる値の範囲を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "2-2r, r=1 または r=-1"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.5
                }
            ]
        }
    ]
};