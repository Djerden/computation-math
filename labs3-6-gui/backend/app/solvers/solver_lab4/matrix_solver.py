def solve_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        max_el = abs(matrix[i][i])
        max_row = i
        for k in range(i+1, n):
            if abs(matrix[k][i]) > max_el:
                max_el = abs(matrix[k][i])
                max_row = k
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        for k in range(i+1, n):
            if matrix[i][i] == 0:
                #ОШИБКА ПРИ ВЫЧИСЛЕНИИ МАТРИЦЫ
                return ''
            c = -matrix[k][i]/matrix[i][i]
            for j in range(i, n+1):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += c * matrix[i][j]
    solution = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        solution[i] = matrix[i][n]/matrix[i][i]
        for k in range(i-1, -1, -1):
            matrix[k][n] -= matrix[k][i] * solution[i]
    return solution
