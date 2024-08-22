import numpy as np

def integrand(quation, x):
    if quation == 1:
        return x ** 2
    if quation == 2:
        return np.sin(x)
    if quation == 3:
        try:
            return 1 / x
        except ZeroDivisionError:
            return "Infinity breaking point at x"


def rectangle_method_left(quation, a, b, e, parts):
    integral = 99999
    answer = []

    while integral > e and parts < 10000000:
        h = (b - a) / parts
        h2 = (b - a) / (parts // 2)

        integral_1 = sum(integrand(quation, a + (i - 1) * h) for i in range(parts))
        integral_2 = sum(integrand(quation, a + (i - 1) * h2) for i in range(parts // 2))

        integral_1 *= h
        integral_2 *= h2

        integral = abs((integral_2 - integral_1) / (2 ** 2 - 1))
        parts *= 2

    if integral_1 < float("inf"):
        answer.append(integral_1)
        answer.append(parts // 2)
        answer.append(integral)
        return answer
    else:
        return "The integral doesn't converge."


def rectangle_method_centre(quation, a, b, e, parts):
    integral = 99999
    answer = []

    while integral > e and parts < 10000000:
        h = (b - a) / parts
        h2 = (b - a) / (parts // 2)

        integral_1 = sum(integrand(quation, a + (i - 1 + h / 2) * h) for i in range(parts))
        integral_2 = sum(integrand(quation, a + (i - 1 + h2 / 2) * h2) for i in range(parts // 2))

        integral_1 *= h
        integral_2 *= h2

        integral = abs((integral_2 - integral_1) / (2 ** 2 - 1))
        parts *= 2

    if integral_1 < float("inf"):
        answer.append(integral_1)
        answer.append(parts // 2)
        answer.append(integral)
        return answer
    else:
        return "The integral doesn't converge."


def rectangle_method_right(quation, a, b, e, parts):
    integral = 99999
    answer = []
    while integral > e and parts < 10000000:
        h = (b - a) / parts
        h2 = (b - a) / (parts // 2)

        integral_1 = sum(integrand(quation, a + (i) * h) for i in range(parts))
        integral_2 = sum(integrand(quation, a + (i) * h2) for i in range(parts // 2))

        integral_1 *= h
        integral_2 *= h2

        integral = abs((integral_2 - integral_1) / (2 ** 2 - 1))
        parts *= 2

    if integral_1 < float("inf"):
        answer.append(integral_1)
        answer.append(parts // 2)
        answer.append(integral)
        return answer
    else:
        return "The integral doesn't converge."


def trapezoidal_method(quation, a, b, e, parts):
    integral = 99999
    answer = []

    while integral > e and parts < 10000000:
        i = 1
        h = (b - a) / parts
        h2 = (b - a) / (parts // 2)
        integral_1 = 0.5 * (
                integrand(quation, a) + integrand(quation, b)
        )
        integral_2 = 0.5 * (
                integrand(quation, a) + integrand(quation, b)
        )

        for i in range(parts // 2):
            integral_2 += integrand(quation, a + i * h2)
        integral_2 *= h2
        i = 1

        for i in range(parts):
            integral_1 += integrand(quation, a + i * h)
        integral_1 *= h

        integral = abs((integral_2 - integral_1) / (2 ** 2 - 1))
        parts *= 2

    if integral_1 < float("inf"):
        answer.append(integral_1)
        answer.append(parts // 2)
        answer.append(integral)
        return answer
    else:
        return "The integral doesn't converge."


def simpson_method(quation, a, b, e, parts):
    integral = 99999
    answer = []

    while integral > e and parts < 10000000:
        h = (b - a) / parts
        h2 = (b - a) / (parts // 2)
        integral_1 = 0
        integral_2 = 0
        x_values = [a + i * h for i in range(parts + 1)]
        x_values_2 = [a + i * h2 for i in range(parts // 2 + 1)]

        integral_2 = integrand(quation, a) + integrand(quation, b)
        for i in range(1, parts // 2, 2):
            integral_2 += 4 * integrand(quation, x_values_2[i])

        for i in range(2, parts // 2 - 1, 2):
            integral_2 += 2 * integrand(quation, x_values_2[i])
        integral_2 *= h2 / 3

        integral_1 = integrand(quation, a) + integrand(quation, b)
        for i in range(1, parts, 2):
            integral_1 += 4 * integrand(quation, x_values[i])
        for i in range(2, parts - 1, 2):
            integral_1 += 2 * integrand(quation, x_values[i])
        integral_1 *= h / 3
        integral = abs((integral_2 - integral_1) / (2 ** 2 - 1))
        parts *= 2

    if integral_1 < float("inf"):
        answer.append(integral_1)
        answer.append(parts // 2)
        answer.append(integral)
        return answer
    else:
        return "The integral doesn't converge."

