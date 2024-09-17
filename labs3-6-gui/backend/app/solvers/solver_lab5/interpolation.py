from app.solvers.solver_lab5.interpolation_util import *

def lagrange_interpolation(x, y, value):
    name = "Метод Лагранжа"
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (value - x[j]) / (x[i] - x[j])
        result += term
    return result


def newton_interpolation_with_shared_difference(x, y, value):
    name = "Метод Ньютона с разделенными разностями"
    n = len(x)
    result = y[0]
    temp = 1.0
    shared_differences_table = create_shared_differences_table(x, y)
    for i in range(1, n):
        temp *= (value - x[i - 1])
        result += temp * (shared_differences_table[0, i])
    return result


def newton_interpolation_with_finite_difference(x, y, inter_point):
    name = "Метод Ньютона с конечными разностями"
    diff_table = create_finite_differences_table(x, y)

    n = len(x)

    h = x[1] - x[0]

    def t_forward(x_val):
        return (x_val - x[0]) / h

    def t_backward(x_val):
        return (x_val - x[-1]) / h

    def forward(x_val):
        result = y[0]
        for i in range(1, n):
            term = diff_table[0][i]
            prod = 1
            for j in range(i):
                prod *= (t_forward(x_val) - j)
            term *= prod / math.factorial(i)
            result += term
        return result

    def backward(x_val):
        result = y[-1]
        for i in range(1, n):
            term = diff_table[-i - 1][i]
            prod = 1
            for j in range(i):
                prod *= (t_backward(x_val) + j)
            term *= prod / math.factorial(i)
            result += term
        return result
    if (x[-1] - x[0]) / 2 < inter_point:
        return forward(inter_point)
    else:
        return backward(inter_point)


def first_interpolation_gauss_form(n, xs, ys, alpha_index, dts, h, fin_diffs, value):
    result = ys[alpha_index]
    t = (value - xs[alpha_index]) / h
    for k in range(1, n):
        term = 1
        for j in range(k):
            term *= t + dts[j]
        result += term * fin_diffs[k][len(fin_diffs[k]) // 2] / math.factorial(k)

    return result


def second_interpolation_gauss_form(n, xs, ys, alpha_index, dts, h, fin_diffs, value):
    result = ys[alpha_index]
    t = (value - xs[alpha_index]) / h
    for k in range(1, n):
        product = 1
        for j in range(k):
            product *= t - dts[j]
        result += product * fin_diffs[k][len(fin_diffs[k]) // 2 - (1 - len(fin_diffs[k]) % 2)] / math.factorial(k)
    return result


def stirling_interpolation(x, y, value):
    name = "Метод Стирлинга"
    n = len(x)
    central_differences_table = create_central_differences_table(y)
    alpha_index = n // 2
    h = x[1] - x[0]
    dts = generate_array_offset(n // 2)
    f1 = first_interpolation_gauss_form(n, x, y, alpha_index, dts, h, central_differences_table, value)
    f2 = second_interpolation_gauss_form(n, x, y, alpha_index, dts, h, central_differences_table, value)
    return (f1 + f2) / 2


def bessel_interpolation(x, y, value):
    n = len(x)
    central_differences_table = create_central_differences_table(y)
    alpha_index = n // 2
    h = x[1] - x[0]
    dts = generate_array_offset(n // 2)
    t = (value - x[alpha_index - 1]) / h
    # print(f"t={t}")
    result = (y[alpha_index - 1] + y[alpha_index]) / 2
    k = 0
    l = 0
    for i in range(1, n):
        if i % 2 == 1:
            current = (t - 0.5)
            for j in range(i - 1):
                current = current * (t + dts[j])

            current /= (math.factorial(i))
            current *= central_differences_table[i][alpha_index - 1 - k]
            result += current
            k += 1
        else:
            current = 1
            for j in range(i):
                current *= (t + dts[j])
            current /= (math.factorial(i))
            current *= (central_differences_table[i][alpha_index - l - 2] + central_differences_table[i][
                alpha_index - 1 - l]) / 2
            l += 1
            result += current

    return result
