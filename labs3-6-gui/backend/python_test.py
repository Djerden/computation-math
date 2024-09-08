import math
from sympy import symbols, Eq, solve


def approximation(pairs):
    answers = []

    try:
        linear_ans = linear(pairs)
        square = polynomial_2(pairs)
        cubic = polynomial_3(pairs)
        exp = exponential(pairs)
        logarithm = logarithmic(pairs)
        gradual = power(pairs)
    except:
        return "Something went wrong: type error"

    answers.append(linear_ans)
    answers.append(square)
    answers.append(cubic)
    answers.append(exp)
    answers.append(logarithm)
    answers.append(gradual)
    return answers


def linear(pairs):
    try:
        n = len(pairs)
        x = [pair[0] for pair in pairs]
        y = [pair[1] for pair in pairs]
        SX = sum(pair[0] for pair in pairs)
        SY = sum(pair[1] for pair in pairs)
        SXX = sum(pair[0] ** 2 for pair in pairs)
        SXY = sum((pair[0] * pair[1]) for pair in pairs)

        delta = SXX * n - SX ** 2
        delta_1 = SXY * n - SX * SY
        delta_2 = SXX * SY - SX * SXY

        a = delta_1 / delta
        b = delta_2 / delta

        P1_x = []
        for pair in pairs:
            P1_x.append(a * pair[0] + b)

        ei = e_i(P1_x, y)  # ???
        S = deviation_S(ei)  # ???
        st_deviation = standart_deviation(ei)
        R = correlation_r(pairs)
        p_i = p(ei, y)

        # return x, y, P1_x, ei, S, R, delta, st_deviation

        # return f"X: {x}\nY: {y}\nP1(x) = {a}x+{b}: {P1_x}\nei: {ei}\nS: {S}\nR: {R}\ndelta: {st_deviation}"
        return [st_deviation, S, f"P1(x) = {a}x + {b}", P1_x, ei, R, p_i, a, b]

    except ValueError:
        return "There are wrong nums, cannot solve approximation"
    except ZeroDivisionError:
        return "There are nums < 0, cannot solve  linear approximation"


def polynomial_2(pairs):
    try:
        x_ = [pair[0] for pair in pairs]
        y_ = [pair[1] for pair in pairs]
        SX = sum(pair[0] for pair in pairs)
        SXX = sum(pair[0] ** 2 for pair in pairs)
        SXXX = sum(pair[0] ** 3 for pair in pairs)
        SXXXX = sum(pair[0] ** 4 for pair in pairs)
        SXXY = sum(pair[0] ** 2 * pair[1] for pair in pairs)
        SXY = sum((pair[0] * pair[1]) for pair in pairs)
        SY = sum(pair[1] for pair in pairs)

        x, y, z = symbols("x y z")
        eq1 = Eq(len(pairs) * x + SX * y + SXX * z, SY)
        eq2 = Eq(SX * x + SXX * y + SXXX * z, SXY)
        eq3 = Eq(SXX * x + SXXX * y + SXXXX * z, SXXY)
        solution = solve((eq1, eq2, eq3), (x, y, z))

        a2 = solution[x]
        a1 = solution[y]
        a0 = solution[z]

        p2_x = []
        for pair in pairs:
            # p2_x.append(a2 * pair[0]**2 + a1 * pair[0] + a0)
            p2_x.append(a0 * pair[0] ** 2 + a1 * pair[0] + a2)

        ei = e_i(p2_x, y_)
        S = deviation_S(ei)  # ???
        st_deviation = standart_deviation(ei)
        R = correlation_r(pairs)
        p_i = p(ei, y_)

        # return f"X: {x_}\nY: {y_}\nP2(x) = {a2}x^2+{a1}x+{a0}: {p2_x}\nei: {ei}\nS: {S}\nR: {R}\ndelta: {st_deviation}"
        # return f"X: {x_}\nY: {y_}\nP2(x) = {a0}x^2+{a1}x+{a2}: {p2_x}\nei: {ei}\nS: {S}\nR: {R}\ndelta: {st_deviation}"
        return [st_deviation, S, f"P2(x) = {a0}x^2 + {a1}x + {a2}", p2_x, ei, p_i, a0, a1, a2]

    except ZeroDivisionError:
        return "There are nums < 0, cannot solve approximation"
    except ValueError:
        return "There are wrong nums, cannot solve approximation"


def polynomial_3(pairs):
    try:
        x_ = [pair[0] for pair in pairs]
        y_ = [pair[1] for pair in pairs]
        SX = sum(pair[0] for pair in pairs)
        SXX = sum(pair[0] ** 2 for pair in pairs)
        SXYY = sum(pair[0] * pair[1] ** 2 for pair in pairs)
        SXXYY = sum(pair[0] ** 2 * pair[1] ** 2 for pair in pairs)
        SXXX = sum(pair[0] ** 3 for pair in pairs)
        SXXXX = sum(pair[0] ** 4 for pair in pairs)
        SXXY = sum(pair[0] ** 2 * pair[1] for pair in pairs)
        SXY = sum((pair[0] * pair[1]) for pair in pairs)
        SY = sum(pair[1] for pair in pairs)

        x, y, z, w = symbols("x y z w")
        eq1 = Eq(len(pairs) * w + SX * x + SXX * y + SXXX * z, SY)
        eq2 = Eq(SX * w + SXX * x + SXXX * y + SXXXX * z, SXY)
        eq3 = Eq(SXX * w + SXXX * x + SXXXX * y + SXXYY * z, SXXY)
        eq4 = Eq(SXXX * w + SXXXX * x + SXXYY * y + SXYY * z, SXXX)

        solution = solve((eq1, eq2, eq3, eq4), (w, x, y, z))

        a3 = solution[w]
        a2 = solution[x]
        a1 = solution[y]
        a0 = solution[z]

        p3_x = []
        for pair in pairs:
            # p2_x.append(a2 * pair[0]**2 + a1 * pair[0] + a0)
            p3_x.append(a3 + a2 * pair[0] + a1 * pair[0] ** 2 + a0 * pair[0] ** 3)

        ei = e_i(p3_x, y_)
        S = deviation_S(ei)  # ???
        st_deviation = standart_deviation(ei)
        R = correlation_r(pairs)
        p_i = p(ei, y_)

        # return f"X: {x_}\nY: {y_}\nP2(x) = {a2}x^2+{a1}x+{a0}: {p2_x}\nei: {ei}\nS: {S}\nR: {R}\ndelta: {st_deviation}"
        # return f"X: {x_}\nY: {y_}\nP2(x) = {a0}x^3+{a1}x^2+{a2}x + {a3}: {p3_x}\nei: {ei}\nS: {S}\nR: {R}\ndelta: {st_deviation}"
        return [st_deviation, S, f"P1(x) = {a0}x^3 + {a1}x^2 + {a2}x + {a3}", p3_x, ei, a0, a1, a2, a3]

    except ZeroDivisionError:
        return "There are nums < 0, cannot solve approximation"
    except ValueError:
        return "There are wrong nums, cannot solve approximation"


def exponential(pairs):
    try:
        x_ = [pair[0] for pair in pairs]
        y_ = [math.log(pair[1]) for pair in pairs]
        SX = sum(pair[0] for pair in pairs)
        SXX = sum(pair[0] ** 2 for pair in pairs)
        SXY = sum((pair[0] * math.log(pair[1])) for pair in pairs)
        SY = sum(math.log(pair[1]) for pair in pairs)

        b = (SY - SX * SXY / SXX) / (len(pairs) - SX * SX / SXX)
        a = (SXY - SX * b) / SXX

        p_x = []
        for pair in pairs:
            p_x.append(a * pair[0] + b)

        ei = e_i(p_x, y_)
        S = deviation_S(ei)
        st_deviation = standart_deviation(ei)
        R = correlation_r(pairs)
        p_i = p(ei, y_)

        # return f"X: {x_}\nY: {y_}\nP2(x) = {a}*log(x)+{b}: {p_x}\nei: {ei}\nS: {S}\nR: {R}\ndelta: {st_deviation}"
        return [st_deviation, S, f"P1(x) = {a}x + ln({b})", p_x, ei, R, p_i, a, b]

    except ValueError:
        return "There are nums < 0, cannot solve logarithmic approximation"
    except ZeroDivisionError:
        return "There are 0 in solution, cannot solve exp approximation"


def logarithmic(pairs):
    try:
        x_ = [math.log(pair[0]) for pair in pairs]
        y_ = [pair[1] for pair in pairs]
        SX = sum(x for x in x_)
        SXX = sum(x ** 2 for x in x_)
        SXY = sum((math.log(pair[0]) * pair[1]) for pair in pairs)
        SY = sum(pair[1] for pair in pairs)

        b = (SY - SX * SXY / SXX) / (len(pairs) - SX * SX / SXX)
        a = (SXY * b) / SXX

        p_x = []
        for pair in pairs:
            p_x.append(a * math.log(pair[0]) + b)

        ei = e_i(p_x, y_)
        S = deviation_S(ei)
        st_deviation = standart_deviation(ei)
        R = correlation_r(pairs)
        p_i = p(ei, y_)

        # return f"X: {x_}\nY: {y_}\nP2(x) = {a}*log(x)+{b}: {p_x}\nei: {ei}\nS: {S}\nR: {R}\ndelta: {st_deviation}"
        return [st_deviation, S, f"P1(x) = {a}ln(x) + {b}", p_x, ei, R, p_i, a, b]

    except ZeroDivisionError:
        return "There are nums < 0, cannot solve approximation"
    except ValueError:
        return "There are nums < 0, cannot solve logarithmic approximation"


def power(pairs):
    try:
        s_x = 0
        s_y = 0
        s_xx = 0
        s_xy = 0
        for pair in pairs:
            x = math.log(pair[0])
            y = math.log(pair[1])
            s_x += x
            s_y += y
            s_xx += x * x
            s_xy += x * y
        x_svg = s_x / len(pairs)
        y_svg = s_y / len(pairs)
        b = (s_y - s_x * s_xy / s_xx) / (len(pairs) - s_x * s_x / s_xx)
        a = (s_xy - s_x * b) / s_xx

        compare = []
        fi = []
        pi = []
        compare_sqr = 0
        for pair in pairs:
            temp = a * math.log(pair[0]) + b
            fi.append(temp)
            e = temp - math.log(pair[1])
            temp2 = e / math.log(pair[1])
            pi.append(temp2)
            compare.append(e)
            compare_sqr += e * e
        tmp_top = 0
        tmp_bottom_left = 0
        tmp_bottom_right = 0
        for pair in pairs:
            tmp_top += (math.log(pair[0]) - x_svg) * (math.log(pair[1]) - y_svg)
            tmp_bottom_left += (math.log(pair[0]) - x_svg) ** 2
            tmp_bottom_right += (math.log(pair[1]) - y_svg) ** 2
        pirson = tmp_top / (tmp_bottom_left * tmp_bottom_right) ** 0.5
        S2 = (compare_sqr / len(pairs)) ** 0.5
        a = round(a, 5)
        # return f"S: {S2} ,{compare_sqr}, P1(x) = {a}ln(x) + {b}: {fi} ,compare,R: {pirson}, pi:{pi}"
        return [
            S2,
            compare_sqr,
            f"P1(x) = {a}ln(x) + {b}",
            fi,
            compare,
            pirson,
            pi,
            a,
            b,
        ]

    except ValueError:
        print("There are nums < 0, cannot solve logarithmic approximation")
    except ZeroDivisionError:
        print("There are 0 in solution, cannot solve gradual approximation")


def e_i(P_x, y):
    e_i = []
    for i in range(len(y)):
        e_i.append(P_x[i] - y[i])
    return e_i


def p(e, y):
    pi = []
    for i in range(len(y)):
        pi.append(e[i] / y[i])
    return pi


def deviation_S(e_i):
    return sum(e ** 2 for e in e_i)


def standart_deviation(e_i):
    n = len(e_i)
    squared_sum = sum(e ** 2 for e in e_i)
    st_dev = math.sqrt(squared_sum / n)
    return st_dev


def correlation_r(pairs):
    n = len(pairs)
    x = [pair[0] for pair in pairs]
    y = [pair[1] for pair in pairs]
    x_ = sum(x) / n
    y_ = sum(y) / n
    r = sum((x[i] - x_) * (y[i] - y_) for i in range(n)) / (
                sum((x[i] - x_) ** 2 for i in range(n)) * sum((y[i] - y_) ** 2 for i in range(n))) ** 0.5
    return r


def main():
    valid_pairs = [[0.4, 2.96], [0.8, 4.98], [1.2, 4.42], [1.6, 2.81], [2, 1.67], [2.4, 1.02], [2.8, 0.66], [3.2, 0.45]]
    result = approximation(valid_pairs)
    for arr in result:
        for i in arr:
            print(i)
        print("------------------------")
        print()
main()