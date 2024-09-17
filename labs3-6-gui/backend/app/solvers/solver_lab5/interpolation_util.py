import numpy as np
import math

def create_finite_differences_table(x, y):
    ##Таблица конечных разностей
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1])

    return table


def output_finite_differences_table(x, y):
    table = create_finite_differences_table(x, y)
    output = "Таблица конечных разностей:\n"

    n = len(table)
    column_width = 12
    for i in range(n):
        output += f'{i:<{column_width}} {x[i]:<{column_width}.3f}'

        for j in range(n - i):
            output += f' {table[i, j]:<{column_width}.3f}'
        output += '\n'

    return output


def create_shared_differences_table(x, y):
    ##Таблица разделенных разностей
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (x[i + j] - x[i])
    return table


def check_finite_differences(x):
    step = x[1] - x[0]
    tolerance = 0  # допустимая погрешность

    for i in range(1, len(x) - 1):
        current_step = x[i + 1] - x[i]
        if not math.isclose(current_step, step, abs_tol=tolerance):
            return False
    return True


def create_central_differences_table(y):
    n = len(y)
    table = [y[:]]

    for k in range(1, n):
        last = table[-1][:]
        table.append(
            [last[i + 1] - last[i] for i in range(n - k)])

    return table


def generate_array_offset(n):
    dts = [0]
    for i in range(1, n + 1):
        dts.append(-i)
        dts.append(i)
    return dts