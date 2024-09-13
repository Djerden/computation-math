from app.solvers.solver_lab4.approximation_computing import *
from app.solvers.solver_lab4.result_builder import *
from app.solvers.solver_lab4.graph_util import *
from app.models.lab4_models import Approximation

round_param = 5
sko_map = {}
func_to_draw = []
func_names_to_draw = []

def linear_result(coordinates_data):
    global func_to_draw
    global  func_names_to_draw
    func_to_draw = []
    func_names_to_draw = []
    name = 'Линейная аппроксимация'
    if linear(coordinates_data) == '':
        # Возвращаем модель
        return Approximation(
            name=name,
            description='Невозможно построить линейную аппроксимацию\n',
        )
    else:
        a, b, cof_cor, S, delta, R_squared, x_coord, y_coord, f, eps = linear(coordinates_data)
        sko_map[name] = delta
        func_to_draw.append(f)
        func_names_to_draw.append(name)

        fline = 'f = ' + str(round(a, round_param)) + ' * x '
        function_for_desmos = str(round(a, round_param)) + ' * x '
        if b >= 0:
            fline += '+ ' + str(round(b, round_param)) + '\n'
            function_for_desmos += '+ ' + str(round(b, round_param))
        else:
            fline += str(round(b, round_param)) + '\n'
            function_for_desmos += str(round(b, round_param))

        fline += 'Коэффициент корреляции Пирсона r = ' + str(round(cof_cor, round_param)) + '\n'
        res = fline + build_result(S, delta, R_squared, x_coord, y_coord, f, eps)
        return Approximation(
            name=name,
            description=res,
            function=function_for_desmos
        )


def squared_result(coordinates_data):
    name = 'Квадратичная аппроксимация'
    t = squared(coordinates_data)
    if t == '':
        if name in sko_map:
            del sko_map[name]
        return Approximation(
            name=name,
            description='Невозможно построить квадратичную аппроксимацию\n'
        )
    elif t == '1':
        if name in sko_map:
            del sko_map[name]
        return Approximation(
            name=name,
            description='Квадратичная аппроксимация сводится к линейной\n'
        )
    else:
        a, b, c, cof_cor, S, delta, R_squared, x_coord, y_coord, f, eps = squared(coordinates_data)
        sko_map[name] = delta
        global func_to_draw
        global func_names_to_draw
        func_to_draw.append(f)
        func_names_to_draw.append(name)

        fline = 'f = ' + str(round(a, round_param)) + ' * x^2'
        function_for_desmos = str(round(a, round_param)) + ' * x^2'
        if b >= 0:
            fline += ' + ' + str(round(b, round_param)) + ' * x'
            function_for_desmos += ' + ' + str(round(b, round_param)) + ' * x'
        else:
            fline += ' ' + str(round(b, round_param)) + ' * x'
            function_for_desmos += ' ' + str(round(b, round_param)) + ' * x'
        if c >= 0:
            fline += ' + ' + str(round(c, round_param))
            function_for_desmos += ' + ' + str(round(c, round_param))
        else:
            fline += ' ' + str(round(c, round_param))
            function_for_desmos += ' ' + str(round(c, round_param))
        fline += '\n'

        res = fline + build_result(S, delta, R_squared, x_coord, y_coord, f, eps)
        return Approximation(
            name=name,
            description=res,
            function=function_for_desmos
        )


def triple_result(coordinates_data):
    name = 'Кубическая аппроксимация'
    t = triple(coordinates_data)
    if t[0] == '':
        if name in sko_map:
            del sko_map[name]
        return Approximation(
            name=name,
            description='Невозможно построить кубическую аппроксимацию\n'
        )
    elif t[0] == '1' and t[1] == 0:
        if name in sko_map:
            del sko_map[name]
        return Approximation(
            name=name,
            description='Кубическая аппроксимация сводится к линейной\n'
        )
    elif t[0] == '1' and t[1] != 0:
        if name in sko_map:
            del sko_map[name]
        return Approximation(
            name=name,
            description='Кубическая аппроксимация сводится к квадратической\n'
        )
    else:
        a, b, c, d, cof_cor, S, delta, R_squared, x_coord, y_coord, f, eps = triple(coordinates_data)
        sko_map[name] = delta
        global func_to_draw
        global func_names_to_draw
        func_names_to_draw.append(name)
        func_to_draw.append(f)
        fline = 'f = ' + str(round(a, round_param)) + ' * x^3 + '
        function_for_desmos = str(round(a, round_param)) + ' * x^3 + '
        if b >= 0:
            fline += ' + ' + str(round(b, round_param)) + ' * x^2'
            function_for_desmos += ' + ' + str(round(b, round_param)) + ' * x^2'
        else:
            fline += ' ' + str(round(b, round_param)) + ' * x^2'
            function_for_desmos += ' ' + str(round(b, round_param)) + ' * x^2'
        if c >= 0:
            fline += ' + ' + str(round(c, round_param)) + ' * x'
            function_for_desmos += ' + ' + str(round(c, round_param)) + ' * x'
        else:
            fline += ' ' + str(round(c, round_param)) + ' * x'
            function_for_desmos += ' ' + str(round(c, round_param)) + ' * x'
        if c >= d:
            fline += ' + ' + str(round(d, round_param))
            function_for_desmos += ' + ' + str(round(d, round_param))
        else:
            fline += ' ' + str(round(d, round_param))
            function_for_desmos += ' ' + str(round(d, round_param))
        fline += '\n'
        res = fline + build_result(S, delta, R_squared, x_coord, y_coord, f, eps)
        return Approximation(
            name=name,
            description=res,
            function=function_for_desmos
        )


def power_result(coordinates_data):
    name = 'Степенная аппроксимация'
    if power(coordinates_data)[0] == '':
        if name in sko_map:
            del sko_map[name]
        return Approximation(
            name=name,
            description='Невозможно построить степенную аппроксимацию\n'
        )
    else:
        a, b, cof_cor, S, delta, R_squared, x_coord, y_coord, f, eps = power(coordinates_data)
        sko_map[name] = delta
        global func_to_draw
        global func_names_to_draw
        func_names_to_draw.append(name)
        func_to_draw.append(f)
        fline = 'f = ' + str(round(a, round_param)) + ' * x ^ ' + str(round(b, round_param))
        function_for_desmos = str(round(a, round_param)) + ' * x^{' + str(round(b, round_param)) + '}'
        fline += '\n'
        res = fline + build_result(S, delta, R_squared, x_coord, y_coord, f, eps)
        return Approximation(
            name=name,
            description=res,
            function=function_for_desmos
        )


def exponential_result(coordinates_data):
    name = 'Экспоненциальная аппроксимация'
    if exponential(coordinates_data)[0] == '':
        if name in sko_map:
            del sko_map[name]
        return Approximation(
            name=name,
            description='Невозможно построить экспоненциальную аппроксимацию\n'
        )
    else:
        a, b, cof_cor, S, delta, R_squared, x_coord, y_coord, f, eps = exponential(coordinates_data)
        sko_map[name] = delta
        global func_to_draw
        global func_names_to_draw
        func_names_to_draw.append(name)
        func_to_draw.append(f)
        fline = 'f = ' + str(round(a, round_param)) + '* e^(x * ' + str(round(b, round_param)) + ')'
        function_for_desmos = str(round(a, round_param)) + '* e^{x * ' + str(round(b, round_param)) + '}'
        fline += '\n'
        res = fline + build_result(S, delta, R_squared, x_coord, y_coord, f, eps)
        return Approximation(
            name=name,
            description=res,
            function=function_for_desmos
        )


def logarithm_result(coordinates_data):
    name = 'Логарифмическая аппроксимация'
    if logarithm(coordinates_data)[0] == '':
        if name in sko_map:
            del sko_map[name]
        return Approximation(
            name=name,
            description='Невозможно построить логарифмическую аппроксимацию\n'
        )
    else:
        a, b, cof_cor, S, delta, R_squared, x_coord, y_coord, f, eps = logarithm(coordinates_data)
        sko_map[name] = delta
        global func_to_draw
        global func_names_to_draw
        func_names_to_draw.append(name)
        func_to_draw.append(f)
        fline = 'f =' + str(round(a, round_param)) + '* ln(x)'
        function_for_desmos = str(round(a, round_param)) + '* \\ln(x)'
        if b > 0:
            fline += ' + ' + str(round(b, round_param))
            function_for_desmos += ' + ' + str(round(b, round_param))
        else:
            fline += str(round(b, round_param))
            function_for_desmos += str(round(b, round_param))
        fline += '\n'
        res = fline + build_result(S, delta, R_squared, x_coord, y_coord, f, eps)
        return Approximation(
            name=name,
            description=res,
            function=function_for_desmos
        )


def best_approx():
    if len(sko_map) != 0:
        best_approximation = min(sko_map, key=sko_map.get)
        return best_approximation
    else:
        return ''


def save_all_functions_graph(x, y):
    global func_to_draw
    global func_names_to_draw
    if len(sko_map)!=0:
        draw_all(x, y, func_to_draw, func_names_to_draw)
