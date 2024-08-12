import random

# Генерируется рандомная матрица с диагональным преобразованием
def generate_random_matrix(n):
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    vector = [float(random.randint(1, 10)) for _ in range(n)]
    
    for i in range(n):
        # Сначала заполним недиагональные элементы и вычислим их сумму модулей
        sum_non_diag = 0
        for j in range(n):
            if i != j:
                matrix[i][j] = float(random.randint(-10, 10))
                sum_non_diag += abs(matrix[i][j])

        # Устанавливаем диагональный элемент так, чтобы он гарантированно был больше суммы модулей недиагональных
        matrix[i][i] = sum_non_diag + random.uniform(1.0, 10)  # Увеличиваем значение на случайную величину для гарантии преобладания

    return matrix, vector

