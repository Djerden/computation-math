import random

# Генерируется рандомная матрица с диагональным преобразованием
def generate_random_matrix(n):
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    vector = [float(random.randint(1, 10)) for _ in range(n)]
    
    for i in range(n):
        # Генерируем сумму для недиагональных элементов, умножаем на 2 для гарантии диагонального преобладания
        sum_non_diag = sum(abs(float(random.randint(-10, 10))) for _ in range(n - 1))
        # Задаем диагональный элемент
        matrix[i][i] = sum_non_diag + float(random.randint(1, 10))
        indices = list(range(n))
        indices.remove(i)  # Исключаем диагональный элемент
        for j in indices:
            matrix[i][j] = float(random.randint(-10, 10))
    
    return matrix, vector

