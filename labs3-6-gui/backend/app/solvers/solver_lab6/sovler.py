import sympy as sp
import numpy as np


def compute_eps_for_multi_step_method(y, y_exact):
    epsilon = abs(y[0] - y_exact[0])
    for i, j in zip(y, y_exact):
        epsilon = max(epsilon, abs(i - j))
    return epsilon

# Функция для замены очень маленьких чисел на ноль
def sanitize_small_numbers(arr, epsilon=1e-10):
    return np.where(np.abs(arr) < epsilon, 0, arr)

def exact_solution(func, x0, y0):
    x = sp.symbols('x')
    y = sp.Function('y')(x)

    ode = sp.Eq(y.diff(x), func(x, y))

    solution = sp.dsolve(ode, y, ics={y.subs(x, x0): y0})

    y_solution = solution.rhs

    y_func = sp.lambdify(x, y_solution, 'numpy')

    # Возвращаем функцию с санитизацией маленьких значений
    def sanitized_y_func(x_values):
        y_values = y_func(x_values)
        return sanitize_small_numbers(y_values)  # Применяем санитизацию

    return sanitized_y_func


def euler(f, y0, x0, xn, h):
    n = int((xn - x0) / h) + 1
    x = np.linspace(x0, xn, n)
    y = np.zeros(n)
    y[0] = y0

    for i in range(n - 1):
        y[i + 1] = y[i] + h * f(x[i], y[i])

    # Применяем санитизацию маленьких значений
    y = sanitize_small_numbers(y)
    return x, y


def runge_kutta_4th(f, y0, x0, xn, h):
    n = int((xn - x0) / h) + 1
    x = np.linspace(x0, xn, n)
    y = np.zeros(n)

    y[0] = y0

    for i in range(n - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + h * k1 / 2)
        k3 = f(x[i] + h / 2, y[i] + h * k2 / 2)
        k4 = f(x[i] + h, y[i] + h * k3)
        y[i + 1] = y[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    # Применяем санитизацию маленьких значений
    y = sanitize_small_numbers(y)
    return x, y


def adams(f, y0, x0, xn, h, eps, k=4):
    x_rk, y_rk, h_2, _ = compute_with_runge_rule(f, y0, x0, x0 + (k - 1) * h, h, eps, "Метод Рунге-Кутта 4го порядка")
    n = int((xn - x0) / h_2) + 1
    x = np.linspace(x0, xn, n)
    y = np.zeros(n)
    for i in range(k):
        y[i] = y_rk[i]

    for i in range(k - 1, n - 1):
        y_pred = y[i] + h_2 / 24 * (
                55 * f(x[i], y[i]) - 59 * f(x[i - 1], y[i - 1]) + 37 * f(x[i - 2], y[i - 2]) - 9 * f(x[i - 3],
                                                                                                     y[i - 3]))
        f_pred = f(x[i + 1], y_pred)
        y_corr = y[i] + h_2 / 24 * (
                9 * f_pred + 19 * f(x[i], y[i]) - 5 * f(x[i - 1], y[i - 1]) + f(x[i - 2], y[i - 2]))

        while abs(y_pred - y_corr) > eps:
            y_pred = y_corr
            y_corr = y[i] + h_2 / 24 * (
                    9 * f_pred + 19 * f(x[i], y[i]) - 5 * f(x[i - 1], y[i - 1]) + f(x[i - 2], y[i - 2]))
        y[i + 1] = y_corr

    # Применяем санитизацию маленьких значений
    y = sanitize_small_numbers(y)
    y_real_solution = exact_solution(f, x0, y0)(x)

    return x, y, y_real_solution


map_methods = {"Метод Эйлера": euler,
               "Метод Рунге-Кутта 4го порядка": runge_kutta_4th,
               "Метод Адамса": adams}


def compute_with_runge_rule(f, y0, x0, xn, h, eps, method_name):
    runge_coefficients = {"Метод Эйлера": 2,
                          "Метод Рунге-Кутта 4го порядка": 15}
    k = runge_coefficients[method_name]
    current_method = map_methods[method_name]
    x, y = current_method(f, y0, x0, xn, h)
    h /= 2
    x_next, y_next = current_method(f, y0, x0, xn, h)
    while abs(y[-1] - y_next[-1]) / k > eps:
        h /= 2
        y = y_next
        x = x_next
        x_next, y_next = current_method(f, y0, x0, xn, h)
    y_real_solution = exact_solution(f, x0, y0)(x_next)

    return x_next, y_next, h, y_real_solution


def compute_adams_method(f, y0, x0, xn, h, eps):
    x_curr, y_curr, y_real_solution = adams(f, y0, x0, xn, h, eps)
    i = 0
    while True:
        if compute_eps_for_multi_step_method(y_curr, y_real_solution) < eps:
            return x_curr, y_curr, y_real_solution
        h /= 2
        x_curr, y_curr, y_real_solution = adams(f, y0, x0, xn, h, eps)
