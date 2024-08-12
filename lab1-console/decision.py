# eps = 0.01
# c = [[2, 2, 10], [10, 1, 1], [2, 10, 1]]
# d = [14, 12, 13]

# Поменять местами строки в матрице.
def _swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

# Поменять местами элементы вектора.
def _swap_vector_elements(vector, index1, index2):
    vector[index1], vector[index2] = vector[index2], vector[index1]

# Проверить условие диагонального преобладания для каждой строки матрицы.
def check_diagonal_dominance(matrix):
    size = len(matrix)
    for i in range(size):
        row_sum = sum(abs(matrix[i][j]) for j in range(size) if i != j)
        if abs(matrix[i][i]) <= row_sum:
            print(f"Диагональный элемент = {matrix[i][i]}, сумма других элементов = {row_sum}")
            return False
    return True

# Привести матрицу к диагональному преобладанию, если это возможно.
def bring_to_diagonal_dominance(matrix, vector):
    size = len(matrix)
    for i in range(size):
        if abs(matrix[i][i]) <= sum(abs(matrix[i][j]) for j in range(size) if i != j):
            for k in range(size):
                if k != i and abs(matrix[k][i]) > sum(abs(matrix[k][j]) for j in range(size) if j != i):
                    _swap_rows(matrix, i, k)
                    _swap_vector_elements(vector, i, k)
                    if check_diagonal_dominance(matrix):
                        return matrix, vector
    if check_diagonal_dominance(matrix):
        return matrix, vector
    else:
        return None, None 

# выражаем x в виде новой матрицы
def get_x(matrix, vector):
    for i in range(len(matrix)): 
        divider = matrix[i][i]
        vector[i] /= divider
        for j in range(len(matrix[i])):
            if i == j: 
                matrix[i][j] = 0
            else: 
                matrix[i][j] = -matrix[i][j]
                matrix[i][j] /= divider
    return matrix, vector

# проверка условия нормы преобразования. Максимальная сумма по строке < 1
def norm_of_transformation(c):
    for i in c:
        if sum(map(abs, i)) >= 1:
            return False
    return True

# Критерий по абсолютным отклонениям
# True - можно выходить из итераций
def absolute_deviations_check(last_iter, current_iter, eps):
    values = []
    for i in range(len(last_iter)):
        values.append(abs(current_iter[i] - last_iter[i]))
    max_value = max(values)
    print('Критерий по абсоютным отклонениям')
    if max_value < eps:
        print(f'max = {max_value} < {eps}')
        print('Заканчиваем вычисления...')
        return True
    else: 
        print(f'max = {max_value} > {eps}')
    return False

# Метод простых итераций 
def simple_iterations(c, d, eps):
    current_d = [0]*len(d)
    last_d = d.copy()
    count_iter = 0
    while count_iter < 25:
        count_iter += 1
        for i in range(len(c)):
            x_i = 0
            for j in range(len(c[i])):
                x_i += c[i][j]*last_d[j]
            x_i += d[i]
            current_d[i] = x_i
        print(f'Итерация #{count_iter}\nПриближение: ')
        print(current_d)
        if absolute_deviations_check(last_d, current_d, eps):
            break 
        last_d = current_d.copy()
    return current_d, count_iter 

def print_matrix_and_vector(matrix, vector):
    print('Матрица:')
    print('[ ', end='')
    print(matrix[0]) 
    for i in range(1, len(matrix)):
        if i == len(matrix)-1:
            print(' ', matrix[i], ']')
        else: 
            print(' ', matrix[i])

    print('Вектор:')
    print(vector)

# Функция обьединяющая все шаги для вывода полноценного решения
def solver(matrix, vector, eps):
    print('Получена матрица и вектор: ')
    print_matrix_and_vector(matrix, vector)
    
    print('Проверка матрицы на диагональное преобладание')
    if not check_diagonal_dominance(matrix):
        print('Матрица не соответствует условию диагонального преобладания. Попытаемся привести...')
        matrix, vector = bring_to_diagonal_dominance(matrix, vector)
        if matrix == None:
            print('Матрицу невозможно привести к диагональному преобладанию')
            return
        print('Матрица приведена к диагональному преобладанию')
        print_matrix_and_vector(matrix, vector) 
    else: 
        print('Матрица соблюдает условие диагонального преобладания')
    
    print('Получаем коэффициенты')
    matrix, vector = get_x(matrix, vector)
    print_matrix_and_vector(matrix, vector)

    if not norm_of_transformation(matrix):
        print('||C|| => 1, не удовлетворяет условию нормы преобразования')
    else: 
        print('||C|| < 1, удовлетворяет условию нормы преобразования')

    answer, iterations = simple_iterations(matrix, vector, eps)
    print('Ответ: ', answer)
    print('Количество итераций: ', iterations)

