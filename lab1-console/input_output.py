from matrix_generator import generate_random_matrix
import sys

def parse_str(string):
    parts = string.strip().split(' | ')
    matrix = list(map(float, parts[0].split()))
    vector = float(parts[1])
    return matrix, vector 

# Ввод с консоли
def console_input():
    print('--Чтение из консоли--')
    
    while True:
        try:    
            eps = float(input('Введите точность (epsilon): ').replace(',', '.'))
            if eps < 0 or eps > 1:
                raise Exception('Значение точности должно быть в пределе от 0 до 1')
            break
        except ValueError:
            print('Введено некорректное значение для точности. Попробуйте еще раз')
        except EOFError:
            print('Выход из программы...')
            sys.exit(0)
        except Exception as e:
            print(f'{e}. Попробуйте еще раз')

    while True: 
        try:
            n = int(input('Введите размерность матрицы (n <= 20): '))
            if n < 1 or n > 20: 
                raise ValueError('Размерность матрицы должна быть в пределах от 1 до 20')
            break
        except ValueError as e:
            print('Ошибка ввода:', e, 'Попробуйте еще раз')
        except EOFError:
            print('Выход из программы...')
            sys.exit(0)
        except Exception as e:
            print(f'{e}. Попробуйте еще раз')
    
            

    matrix = []
    vector = []
    print('Построчно введите коэффициенты матрицы и вектора в формате "a11 a12 a13 ... a1n | b1"')
    for i in range(n):
        while True: 
            try:
                user_input = input()
                a, b = parse_str(user_input.replace(',', '.'))
                if len(a) != n:
                    raise ValueError('Размерность матрицы не совпадает с количеством коэффициентов в строке')
                matrix.append(a)
                vector.append(b)
                break 
            except ValueError as e:
                print('Ошибка формата ввода', {e}, 'Попробуйте ввести эту же строку еще раз')
            except IndexError as e:
                print('Ошибка формата ввода', {e}, 'Попробуйте ввести эту же строку еще раз')
            except EOFError:
                print('Выход из программы...')
                sys.exit(0)
            except Exception as e:
                print(f'{e}. Попробуйте еще раз')
    return matrix, vector, eps

# Ввод из файла
def file_input():
    print('--Чтение из файла--') 
    print('Первым значением должна подаваться точность (epsilon)')
    print('Максимальная размерность матрицы <= 20')
    print('Матрица в файле должна иметь следующий вид:\n', 
        '\t', 'a11 a12 a13 ... a1n | b1', '\n',
        '\t', 'a21 a22 a23 ... a2n | b2', '\n',
        '\t', '... ... ... ... ... | ...', '\n',
        '\t', 'an1 an2 an3 ... ann | bn', '\n')
    
    try:
        path = input('Введите абсолютный путь до файла: ')
        matrix = []
        vector = []
        eps = 0
        with open(path, mode='r', encoding="UTF-8") as file:
            eps = float(file.readline().strip().replace(',', '.'))
            if eps < 0 or eps > 1:
                raise Exception('Значение точности должно быть в пределе от 0 до 1')
            for line in file:
                if not line.strip():  # Если строка пуста или содержит только пробелы/перенос строки
                    break
                a, b = parse_str(line.replace(',', '.'))
                matrix.append(a)
                vector.append(b)
        for i in matrix:
            if len(i) != len(matrix):
                raise ValueError('Матрица должна быть квадратной')
    except FileNotFoundError:
        print("Файл не найден")
        return None, None, None
    except ValueError as e:
        print(f"Ошибка в данных файла, проверьте корректность содержания: {e}")
        return None, None, None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None, None, None


    return matrix, vector, eps

# Генерирование рандомной матрицы
def random_matrix_input():
    print('--Генерирование случайной матрицы--')
    
    while True: 
        try:    
            eps = float(input('Введите точность (epsilon): ').replace(',', '.'))
            if eps < 0 or eps > 1:
                raise Exception('Значение точности должно быть в пределе от 0 до 1')
            break
        except ValueError:
            print('Введено некорректное значение для точности. Попробуйте еще раз') 
        except EOFError:
            print('Выход из программы...')
            sys.exit(0)
        except Exception as e:
            print(f'Ошибка ввода: {e}. Попробуйте еще раз')   
    
    while True:
        try:    
            n = int(input('Введите размерность матрицы (n <= 20): '))
            if n < 1 or n > 20: 
                raise ValueError('Размерность матрицы должна быть в пределах от 1 до 20')
            break
        except ValueError as e:
            print("Ошибка ввода:", e)  
        except EOFError:
            print('Выход из программы...')
            sys.exit(0)
        except Exception as e:
            print(f'{e}. Попробуйте еще раз')   
    
    matrix, vector = generate_random_matrix(n)    
    return matrix, vector, eps


