from app.solvers.solver_lab6.data_parser import *
from app.solvers.solver_lab6.validator import *
from app.solvers.solver_lab6.sovler import *
from tabulate import tabulate
from app.solvers.solver_lab6.functions import *

from app.models.lab6_models import DataForGraphics

def exact_sol(x_data, y_data, function):
    x_exact = np.linspace(min(x_data), max(x_data), 1000)
    y_exact = exact_solution(function, x_data[0], y_data[0])(x_exact)
    return x_exact, y_exact

def solve(y0, x0, xn, h, eps, func):

    if func == "y' = x^2 - 2y":
        function = function1
    elif func == "y' = x + 1 / (1 + y^2)":
        function = function2
    elif func == "y' = 2x - 3y":
        function = function3
    else:
        return "", []

    result1, graph1 = euуer_method(function, y0, x0, xn, h, eps)
    result2, graph2 = runge_kutta_method(function, y0, x0, xn, h, eps)
    result3, graph3 = adams_method(function, y0, x0, xn, h, eps)

    result_output = result1 + result2 + result3
    list_of_graphics = [graph1, graph2, graph3]
    return result_output, list_of_graphics

# Метод Эйлера
def euуer_method(function, y0, x0, xn, h, eps):
    name = 'Метод Эйлера'
    result = ''
    x_euler, y_euler, usls, y_real_solution = compute_with_runge_rule(function, y0, x0, xn, h, eps,name)
    result += name + '\n'
    headers = ["X", "Y", "Точное решение"]
    data = list(zip(x_euler, y_euler, y_real_solution))
    result += tabulate(data, headers=headers, tablefmt="grid")
    exact_x, exact_y = exact_sol(x_euler, y_euler, function)
    return result, DataForGraphics(name=name, method_x=x_euler, method_y=y_euler, exact_x=exact_x, exact_y=exact_y)

# Метод Рунге-Кутта
def runge_kutta_method(function, y0, x0, xn, h, eps):
    name = 'Метод Рунге-Кутта'
    result = ''
    x_runge_kutta, y_runge_kutta, h1, y_real_solution = compute_with_runge_rule(function, y0, x0, xn, h, eps,"Метод Рунге-Кутта 4го порядка")
    result += '\n\n' + name + '\n'
    headers = ["X", "Y", "Точное решение"]
    data = list(zip(x_runge_kutta, y_runge_kutta, y_real_solution))
    result += tabulate(data, headers=headers, tablefmt="grid")
    exact_x, exact_y = exact_sol(x_runge_kutta, y_runge_kutta, function)
    return result, DataForGraphics(name=name, method_x=x_runge_kutta, method_y=y_runge_kutta, exact_x=exact_x, exact_y=exact_y)

# Метод Адамса
def adams_method(function, y0, x0, xn, h, eps):
    name = 'Метод Адамса'
    result = ''
    x_adams, y_adams, y_real_solution = compute_adams_method(function, y0, x0, xn, h, eps)
    result += '\n\n' + name + '\n'
    headers = ["X", "Y", "Точное решение"]
    data = list(zip(x_adams, y_adams, y_real_solution))
    result += tabulate(data, headers=headers, tablefmt="grid")
    exact_x, exact_y = exact_sol(x_adams, y_adams, function)
    return result, DataForGraphics(name=name, method_x=x_adams, method_y=y_adams, exact_x=exact_x, exact_y=exact_y)