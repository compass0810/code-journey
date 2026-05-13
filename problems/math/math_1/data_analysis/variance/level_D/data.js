window.practiceData = window.practiceData || {};
window.practiceData["math/math_1/data_analysis/variance/level_D"] = {
    "chapters": [
        {
            "title": "データの分析",
            "lessons": [
                {
                    "id": "math-math_1-data_analysis-variance-level_D-7822b226-7277-49dd-bfd4-25f55c0ffeec",
                    "title": "データの追加と分散の変動範囲",
                    "instruction": "n個（n≧3）の実数からなるデータA = {x_1, x_2, ..., x_n}があり、その平均値をx_bar、分散をs^2 (s > 0)とする。このデータ群に、新たにデータx_{n+1}を追加してn+1個のデータからなるデータB = {x_1, x_2, ..., x_n, x_{n+1}}を作成する。ここで、x_{n+1}は集合Aの要素のいずれか一つと同じ値をとるものとする（x_{n+1} ∈ {x_1, x_2, ..., x_n}）。このとき、データBの分散s'^2とデータAの分散s^2の比 r = s'^2/s^2 がとり得る値の範囲をnを用いて表せ。",
                    "answers": [
                        "n/(n+1) <= r <= 2n^2/(n+1)^2"
                    ],
                    "matchType": "exact",
                    "serial_number": "数学I No.76",
                    "subject_display": "数学I",
                    "difficulty": 9.5
                },
                {
                    "id": "math-math_1-data_analysis-variance-level_D-b4080c26-1cea-43d9-a619-1a158e6c5536",
                    "serial_number": "数学I No.77",
                    "title": "分散の最小値とデータの条件",
                    "instruction": "nを3以上の自然数とする。n個のデータ x_1, x_2, ..., x_n の平均値を m、分散を s^2 とする。各データは 0≦x_i≦1 を満たす実数である。このとき、以下の問いに答えよ。\n(1) 分散 s^2 が最大となる平均値 m の値を n を用いて表せ。\n(2) 分散 s^2 のとりうる値の範囲を n を用いて表せ。\n(3) ある定数 k に対して、すべての i について |x_i - m| ≦ k が成り立つとき、分散 s^2 ≦ k^2 が成立することを証明し、さらに s^2 が k^2 となるための必要十分条件を、データの値 x_i を用いて述べよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "(1) 1/2, (2) 0≦s^2≦1/4, (3) x_iがk+mまたは-k+mのみの値をとる"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.9
                },
                {
                    "id": "math-math_1-data_analysis-variance-level_D-aee8fe9a-c9aa-4825-97fe-b1315ad52623",
                    "serial_number": "数学I No.78",
                    "title": "分散の最小値と変数の決定",
                    "instruction": "nを3以上の整数とする。n個のデータ x_1, x_2, ..., x_n は、すべての要素が 0 以上の整数であり、その平均値が 4 であるとする。このデータの分散 s^2 が最大となるようなデータの組 (x_1, x_2, ..., x_n) を考えるとき、その分散 s^2 の最大値を n を用いて表せ。ただし、データの中に 0 が少なくとも1つ含まれるものとする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "16(n-1)/n"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.9
                },
                {
                    "id": "math-math_1-data_analysis-variance-level_D-0ac4f319-f6cd-4e8e-8800-5dd80f8adeba",
                    "serial_number": "数学I No.79",
                    "title": "分散の最小値と定数の決定",
                    "instruction": "n個のデータx_1, x_2, ..., x_nがあり、その平均値をm、分散をvとする。また、各データに対してy_i = x_i - a (i=1, 2, ..., n) となるデータy_1, y_2, ..., y_nを考える。n=5であり、データが x_1=1, x_2=2, x_3=3, x_4=4, x_5=a であるとき、y_1, y_2, y_3, y_4, y_5 の分散をV(a)とする。V(a)が最小となるような定数aの値と、そのときの最小値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "a=2.5, V(a)=1.5"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.9
                },
                {
                    "id": "math-math_1-data_analysis-variance-level_D-ed6f9f80-26ac-4558-a06b-04d16a437bdc",
                    "serial_number": "数学I No.80",
                    "title": "分散の最小値と変数の制約",
                    "instruction": "n個の実数データ x_1, x_2, ..., x_n (n≧3) があり、その平均値を μ とする。各データは 0 ≦ x_i ≦ 1 を満たしている。このとき、分散 s^2 = (1/n) Σ(x_i - μ)^2 のとりうる値の最大値を、nを用いて表せ。\nなお、各データは自由に選べるものとする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "1/4"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.9
                },
                {
                    "id": "math-math_1-data_analysis-variance-level_D-8244540d-286f-4820-a1b4-bfc11eb215fe",
                    "serial_number": "数学I No.81",
                    "title": "分散の最小値とデータの条件",
                    "instruction": "nを3以上の整数とし、n個の実数データx_1, x_2, ..., x_nの平均値をm、分散をvとする。すべてのデータが0以上であるとき、以下の条件を同時に満たすようなデータが存在するためのmの範囲を求めよ。\n(1) m = 1\n(2) v = 1 - (1/n)\n\nこのとき、データのうち少なくとも何個が0であるかをnを用いて表せ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "n-1"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.9
                },
                {
                    "id": "math-math_1-data_analysis-variance-level_D-b09ac0fd-e600-40f5-8641-698df98600ed",
                    "serial_number": "数学I No.365",
                    "subject_display": "数学I",
                    "title": "分散の最小値と変数の決定",
                    "instruction": "n個のデータ x_1, x_2, ..., x_n (n≧3) があり、その平均値を m とする。各データは x_i ∈ {0, 1, 2} を満たし、0, 1, 2 をとるデータの個数をそれぞれ a, b, c とする。a+b+c=n であり、平均値 m が 4/3 であるとき、このデータの分散 s^2 を最小にするような組 (a, b, c) をすべて求めよ。また、そのときの最小値を n を用いて表せ。\nなお、分散 s^2 は s^2 = (1/n) Σ(x_i - m)^2 で定義される。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "(a, b, c) = (n/6, 2n/3, n/6) のとき最小値 2/3"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.9
                }
            ]
        },
        {
            "title": "データ分析",
            "lessons": [
                {
                    "id": "math-math_1-data_analysis-variance-level_D-e9d53680-f7bb-4595-8bf9-917471bca45d",
                    "serial_number": "数学I No.82",
                    "title": "分散の最小値と変数の決定",
                    "instruction": "n個のデータx_1, x_2, ..., x_nがあり、その平均値が0、分散が4であるとする。これらに対して、新たなデータy_i = x_i + a (i=1, 2, ..., n) を考える。また、別のデータz_i = b*x_i (i=1, 2, ..., n) を考える。y_1, ..., y_n の平均値を0とし、y_1, ..., y_n の分散と z_1, ..., z_n の分散の和が16であるとき、正の定数bの値を求めよ。ただし、n≧2とする。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "sqrt(3)"
                    ],
                    "matchType": "exact",
                    "subject_display": "数学I",
                    "difficulty": 9.9
                },
                {
                    "id": "math-math_1-data_analysis-variance-level_D-32c70e13-7629-4358-9879-184b0b1d1eb7",
                    "serial_number": "数学I No.316",
                    "subject_display": "数学I",
                    "title": "分散の最小値と変量の変換",
                    "instruction": "n個のデータ x_1, x_2, ..., x_n (n≧2) があり、その平均値をx_bar、分散をs^2とする。すべてのデータに対して x_i' = ax_i + b (a, bは定数、a > 0) と変換したとき、変換後のデータの分散がs^2と一致し、かつ変換後のデータの平均値x_bar'が0となった。このとき、次の問いに答えよ。\n(1) bをx_barとaを用いて表せ。\n(2) 変換後のデータ x_i' が、平均値が0、分散が1であるような標準化されたデータ y_i = (x_i - x_bar)/s に一致するための a の値を求めよ。\n(3) a, bが (2) で求めた値であるとき、元のデータの分散 s^2 を用いて、Σ_{i=1}^{n} (x_i' - y_i)^2 の値を求めよ。",
                    "content": "",
                    "choices": [],
                    "answers": [
                        "0"
                    ],
                    "matchType": "exact",
                    "difficulty": 9.7
                }
            ]
        }
    ]
};