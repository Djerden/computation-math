from app.solvers.solver_lab5.data_parser import *
from app.solvers.solver_lab5.validator import *

from app.solvers.solver_lab5.interpolation import *
from app.solvers.solver_lab5.graph import *
from app.models.lab5_models import DataForGraph
def solve_interpolation(x, y, inter_point):
    result_output = ''
    result_output += output_finite_differences_table(x, y)

    lagrange = lagrange_results(x, y, inter_point)
    newton_1 = newton_interpolation_with_shared_difference_results(x, y, inter_point)
    newton_2 = newton_interpolation_with_finite_difference_results(x, y, inter_point)
    stirling = stirling_interpolation_results(x, y, inter_point)
    bessel = bessel_interpolation_results(x, y, inter_point)

    # Конкатенация всех result'ов
    result_output += lagrange['result']
    result_output += newton_1['result']
    result_output += newton_2['result']
    result_output += stirling['result']
    result_output += bessel['result']

    # Создание списка объектов DataForGraph
    graphs = [
        DataForGraph(name=lagrange['name'], x=lagrange['x'], y=lagrange['y'], inter_point=lagrange['inter_point']),
        DataForGraph(name=newton_1['name'], x=newton_1['x'], y=newton_1['y'], inter_point=newton_1['inter_point']),
        DataForGraph(name=newton_2['name'], x=newton_2['x'], y=newton_2['y'], inter_point=newton_2['inter_point']),
        DataForGraph(name=stirling['name'], x=stirling['x'], y=stirling['y'], inter_point=stirling['inter_point']),
        DataForGraph(name=bessel['name'], x=bessel['x'], y=bessel['y'], inter_point=bessel['inter_point']),
    ]

    return result_output, graphs


# Метод Лагранжа
def lagrange_results(x, y, inter_point):
    name = 'Метод Лагранжа'
    result = ''
    xs = []
    ys = []
    interpolation_point = [inter_point]

    lagrange_result = lagrange_interpolation(x, y, inter_point)
    xs, ys = generate_data_for_graphik(x, y, lagrange_interpolation)
    interpolation_point.append(lagrange_result)
    result += '\n' + 'Метод Лагранжа: ' + str(lagrange_result) + '\n'
    return {
        'name': name,
        'result': result,
        'x': xs,
        'y': ys,
        'inter_point': interpolation_point
    }

# Метод Ньютона с разделенными разностями (шаг не равен константе)
def newton_interpolation_with_shared_difference_results(x, y, inter_point):
    name = 'Метод Ньютона с разделенными разностями'
    result = ''
    xs = []
    ys = []
    interpolation_point = [inter_point]

    if not check_finite_differences(x):
        newton_shared_result = newton_interpolation_with_shared_difference(x, y, inter_point)
        if newton_shared_result is not None:
            xs, ys = generate_data_for_graphik(x, y, newton_interpolation_with_shared_difference)
            interpolation_point.append(newton_shared_result)

            result += '\n' + 'Метод Ньютона с разделенными разностями: ' + str(newton_shared_result) + '\n'
    else:
        result += '\n' + 'Невозможно построить интерполяционный многочлен Ньютона с разделенными разностями \nиз-за некорректных входных данных\n' + 'Проверьте значения x, они не должны быть равноотстоящими\n'
    return {
        'name': name,
        'result': result,
        'x': xs,
        'y': ys,
        'inter_point': interpolation_point
    }


# Метод Ньютона с конечными разностями (точки располагаются с одинаковым шагом)
def newton_interpolation_with_finite_difference_results(x, y, inter_point):
    name = 'Метод Ньютона с конечными разностями'
    result = ''
    xs = []
    ys = []
    interpolation_point = [inter_point]

    if check_finite_differences(x):
        newton_finite_result = newton_interpolation_with_finite_difference(x, y, inter_point)
        if newton_finite_result is not None:
            xs, ys = generate_data_for_graphik(x, y, newton_interpolation_with_finite_difference)
            interpolation_point.append(newton_finite_result)

            result += '\n' + 'Метод Ньютона с конечными разностями: ' + str(newton_finite_result) + '\n'
    else:
        result += '\n' + 'Невозможно построить интерполяционный многочлен Ньютона с конечнми разностями \nиз-за некорректных входных данных\n' + 'Проверьте значения x, они должны быть равноотстоящими\n'
    return {
        'name': name,
        'result': result,
        'x': xs,
        'y': ys,
        'inter_point': interpolation_point
    }

# Метод Стирлинга
def stirling_interpolation_results(x, y, inter_point):
    name = 'Метод Стирлинга'
    result = ''
    xs = []
    ys = []
    interpolation_point = [inter_point]

    if len(x) % 2 == 1 and check_finite_differences(x):
        stirling_result = stirling_interpolation(x, y, inter_point)
        if stirling_result is not None:
            xs, ys = generate_data_for_graphik(x, y, stirling_interpolation)
            interpolation_point.append(stirling_result)
            result += '\n' + 'Метод Стирлинга: ' + str(stirling_result) + '\n'
    else:
        result += '\n' + 'Невозможно построить интерполяционный многочлен Стирлинга \nиз-за некорректных входных данных\n' + 'Проверьте значения x, они должны быть равноотстоящими\n и их количество должно быть нечетным\n'
    return {
        'name': name,
        'result': result,
        'x': xs,
        'y': ys,
        'inter_point': interpolation_point
    }

# Метод Бессяля
def bessel_interpolation_results(x, y, inter_point):
    name = 'Метод Бесселя'
    result = ''
    xs = []
    ys = []
    interpolation_point = [inter_point]

    if len(x) % 2 == 0 and check_finite_differences(x):
        bessel_result = bessel_interpolation(x, y, inter_point)
        if bessel_result is not None:
            xs, ys = generate_data_for_graphik(x, y, bessel_interpolation)
            interpolation_point.append(bessel_result)
            result += '\n' + 'Метод Бесселя: ' + str(bessel_result) + '\n'
    else:
        result += '\n' + 'Невозможно построить интерполяционный многочлен Бесселя \nиз-за некорректных входных данных\n' + 'Проверьте значения x, они должны быть равноотстоящими\n и их количество должно быть четным\n'

    return {
        'name': name,
        'result': result,
        'x': xs,
        'y': ys,
        'inter_point': interpolation_point
    }