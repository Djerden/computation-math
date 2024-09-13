import math
from app.solvers.solver_lab4.matrix_solver import *
from app.solvers.solver_lab4.approximation_computing_util import *


def lin_approx(x_coord, y_coord):
    matrix = [[sum([i*i for i in x_coord]), sum(x_coord), sum([x*y for x, y in zip(x_coord, y_coord)])], [sum(x_coord), len(x_coord), sum(y_coord)]]
    solve = solve_matrix(matrix)
    if solve == '':
        return ['']
    a = solve[0]
    b = solve[1]
    return a, b


def linear(coordinates):
    try:
        x_coord = coordinates[0]
        y_coord = coordinates[1]
        a, b = lin_approx(x_coord, y_coord)
        f = [a * x + b for x in x_coord]
        eps, delta, S, SS_total, R_squared = aprox_staff_computing(x_coord, y_coord, f)
        return a, b, cof_cor(x_coord, y_coord), S, delta, R_squared, x_coord, y_coord, f, eps
    except BaseException:
        return ['']


def squared(coordinates):
    try:
        x_coord = coordinates[0]
        y_coord = coordinates[1]
        matrix = [[sum([x ** 4 for x in x_coord]), sum([x ** 3 for x in x_coord]), sum([x ** 2 for x in x_coord]),
                   sum([x ** 2 * y for x, y in zip(x_coord, y_coord)])],
                  [sum([x ** 3 for x in x_coord]), sum([x ** 2 for x in x_coord]), sum(x_coord),
                   sum([x * y for x, y in zip(x_coord, y_coord)])],
                  [sum([x ** 2 for x in x_coord]), sum(x_coord), len(x_coord), sum(y_coord)]]
        a, b, c = solve_matrix(matrix)
        f = [a*x ** 2 + b * x + c for x in x_coord]
        if a == 0:
            return '1'
        eps, delta, S, SS_total, R_squared = aprox_staff_computing(x_coord, y_coord, f)
        return a, b, c, cof_cor(x_coord, y_coord), S, delta, R_squared, x_coord, y_coord, f, eps
    except BaseException:
        return ['']


def triple(coordinates):
    try:
        x_coord = coordinates[0]
        y_coord = coordinates[1]
        matrix = [[sum([x ** 6 for x in x_coord]), sum([x ** 5 for x in x_coord]), sum([x ** 4 for x in x_coord]),
                   sum([x ** 3 for x in x_coord]), sum([x ** 3 * y for x, y in zip(x_coord, y_coord)])],
                  [sum([x ** 5 for x in x_coord]), sum([x ** 4 for x in x_coord]), sum([x ** 3 for x in x_coord]),
                   sum([x ** 2 for x in x_coord]), sum([x ** 2 * y for x, y in zip(x_coord, y_coord)])],
                  [sum([x ** 4 for x in x_coord]), sum([x ** 3 for x in x_coord]), sum([x ** 2 for x in x_coord]),
                   sum(x_coord), sum([x * y for x, y in zip(x_coord, y_coord)])],
                  [sum([x ** 3 for x in x_coord]), sum([x ** 2 for x in x_coord]), sum(x_coord), len(x_coord),
                   sum(y_coord)]]
        a, b, c, d = solve_matrix(matrix)
        if a == 0:
            return ['1',b]
        f = [a*x**3+b*x**2+c*x+d for x in x_coord]
        eps, delta, S, SS_total, R_squared = aprox_staff_computing(x_coord, y_coord, f)
        return a, b, c, d, cof_cor(x_coord, y_coord), S, delta, R_squared, x_coord, y_coord, f, eps
    except BaseException:
        return ''


def power(coordinates):
    try:
        x_coord = coordinates[0]
        y_coord = coordinates[1]
        if check_less_zero(x_coord) and (check_less_zero(y_coord)):
            x_coord_log = [math.log(x) for x in x_coord]
            y_coord_log = [math.log(y) for y in y_coord]
        else:
            return ['']
        b, a = lin_approx(x_coord_log, y_coord_log)
        a = math.exp(a)
        f = [a*(x**b) for x in x_coord]
        eps, delta, S, SS_total, R_squared = aprox_staff_computing(x_coord, y_coord, f)
        return a, b, cof_cor(x_coord, y_coord), S, delta, R_squared, x_coord, y_coord, f, eps
    except BaseException:
        return ['']


def exponential(coordinates):
    try:
        x_coord = coordinates[0]
        y_coord = coordinates[1]
        if check_less_zero(y_coord):
            y_coord_log = [math.log(y) for y in y_coord]
        else:
            return ['']
        b, a = lin_approx(x_coord, y_coord_log)
        a = math.exp(a)
        f = [a * (math.exp(x*b)) for x in x_coord]
        eps, delta, S, SS_total, R_squared = aprox_staff_computing(x_coord, y_coord, f)
        return a, b, cof_cor(x_coord, y_coord), S, delta, R_squared, x_coord, y_coord, f, eps
    except BaseException:
        return ['']


def logarithm(coordinates):
    try:
        x_coord = coordinates[0]
        y_coord = coordinates[1]
        if check_less_zero(x_coord):
            x_coord_log = [math.log(x) for x in x_coord]
        else:
            return ['']
        a, b = lin_approx(x_coord_log, y_coord)
        f = [a * x + b for x in x_coord_log]
        eps, delta, S, SS_total, R_squared = aprox_staff_computing(x_coord, y_coord, f)
        return a, b, cof_cor(x_coord, y_coord), S, delta, R_squared, x_coord, y_coord, f, eps
    except BaseException:
        return ['']