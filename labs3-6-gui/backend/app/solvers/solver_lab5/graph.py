def generate_data_for_graphik(x, y, interpolation_func):
    xs, ys = [], []
    dx = 0.1
    a = x[0] - dx
    b = x[-1] + dx
    i = a
    while i <= b:
        # Добавляем проверку на малое значение для i
        if abs(i) < 1e-12:
            i = 0.0

        xs.append(i)
        ys.append(interpolation_func(x, y, i))
        i += dx
    return xs, ys

