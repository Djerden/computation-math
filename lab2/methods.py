import numpy as np

def example_func(x):
    return x**3 - x + 4

# Метод половинного деления
def half_division_method(func, a, b, eps):
    n = 0
    n_limit = int(np.log2(abs(a-b)/eps)) + 1 
    print(n_limit)
    x = (a+b)/2
    while (abs(a-b) > eps or abs(func(x)) >= eps) and n != n_limit:
        if func(a)*func(x) > 0:
            a = x
        else: 
            b = x
        x = (a + b)/2
        n += 1
        print(f'a = {round(a, 5)}, b = {round(b, 5)}, x = {round(x, 5)}, f(a) = {round(func(a), 5)}, f(b) = {round(func(b), 5)}, f(x) = {round(func(x), 5)}, |a-b| = {abs(a-b)}')
    return x, func(x), n


# Метод Ньютона
def newton_method(func, a, b, eps):
    pass

# Метод простой итреации 
def simple_iteration():
    pass

# Метод простой итерации для системы нелинейных уравнений
def simple_iteration_system():
    pass


if __name__ == "__main__":
    # print(half_division_method(example_func, -2, -1, 0.01))
    # print(newton_method(example_func, -2, -1, 0.01))
    print()