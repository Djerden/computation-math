from decision import solver
from input_output import console_input, file_input, random_matrix_input

def console():
    matrix, vector, eps = console_input()
    solver(matrix, vector, eps)

def file():
    matrix, vector, eps = file_input()
    if matrix == None or vector == None or eps == None:
        return 
    solver(matrix, vector, eps)

def random_matrix():
    matrix, vector, eps = random_matrix_input()
    solver(matrix, vector, eps)


print('Решение Слау методом простых итераций')

while True:
    print('-----------------------------------------------')
    print('Справка по командам:')
    print('\tСчитать матрицу с консоли - "1"')
    print('\tСчитать матрицу из файла - "2"')
    print('\tСгенерировать случайную матрицу - "3"')
    print('\tВыйти из программы - "4"')
    print('-----------------------------------------------')
    choice = input('Введите команду: ').strip()
    match(choice):  
        case '1':
            console()
        case '2':
            file()
        case '3':
            random_matrix()
        case '4':
            print('Завершение программы...')
            break
        case _:
            print('Ввод не распознан, попробуй снова') 
