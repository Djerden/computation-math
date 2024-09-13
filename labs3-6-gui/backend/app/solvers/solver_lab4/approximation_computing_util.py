from math import sqrt


def evaluate_approximation(R):
    if R >= 0.95:
        return "Высокая точность аппроксимации (модель хорошо описывает явление)"
    elif 0.75 <= R < 0.95:
        return "Удовлетворительная аппроксимация (модель в целом адекватно описывает явление)"
    elif 0.5 <= R < 0.75:
        return "Слабая аппроксимация (модель слабо описывает явление)"
    else:
        return "Точность аппроксимации недостаточна, модель требует изменения"


def cof_cor(x_coord, y_coord):
    x_average = sum(x_coord)/len(x_coord)
    y_average = sum(y_coord)/len(y_coord)
    numerator = 0
    denominator_x = 0
    denominator_y = 0
    for x, y in zip(x_coord, y_coord):
        numerator += (x - x_average) * (y - y_average)
        denominator_x += (x - x_average) ** 2
        denominator_y += (y - y_average) ** 2
    return numerator / sqrt(denominator_x * denominator_y)


def check_less_zero(arr):
    for i in range(len(arr)):
        if arr[i] <= 0:
            return False
    return True


def aprox_staff_computing(x_coord, y_coord, f):
    eps = [y - f for y, f in zip(y_coord, f)]
    # СКО
    delta = (sum([i * i for i in eps]) / len(x_coord)) ** 0.5

    # мера отклонения
    S = sum([i * i for i in eps])
    # Коэффициент детерминации
    y_average = sum(f) / len(f)
    #    SS_total = sum((y_coord - y_average) ** 2)
    SS_total = sum((y - y_average) ** 2 for y in y_coord)

    if SS_total == 0:
        return ''
    # Коэффициент детерминации
    R_squared = 1 - (S / SS_total)

    return eps, delta, S, SS_total, R_squared