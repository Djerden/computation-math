import colors as color
import solvers
from art import tprint

tprint('Lab 2', font='bulbhead')

print(color.BOLD + color.RED, "Решатель Нелинейных Уравнений!", color.END)

while True:
    try:
        print('\n', color.UNDERLINE + color.YELLOW + "Выберите уравнение или выход (цифра):" + color.END)
        
        print('\t Нелинейные уравнения:', '\n',
              color.GREEN,
              '\t\t', "1: x^2 - 3 = 0", '\n',
              '\t\t', "2: 5/x - 2x = 0", '\n',
              '\t\t', "3: e^(2x) - 2 = 0", '\n',
              '\t\t', "4: -1.8x^3 - 2.94x^2 + 10.37x + 5.38 = 0", '\n', 
              color.END, 
              '\tСистемы нелинейных уравнений:\n', 
              color.GREEN, 
              '\t\t', "5: 0.3 - 0.1x^2 - 0.2y^2", '\n',
              '\t\t', "   0.7 - 0.2x^2 - 0.1xy", '\n',
              '\t\t', "6: 3y^2 + 0.5", '\n',
              '\t\t', "   sin(x)^2", '\n',
              color.END, 
              '\tДругие опции:\n', 
              color.GREEN, 
              '\t\t', "7: Выход",
              color.END)

        choice = int(input("Вариант: ").strip())
        if choice == 1:
            new_input = solvers.Input(1)
            del new_input
            continue
        elif choice == 2:
            new_input = solvers.Input(2)
            del new_input
            continue
        elif choice == 3:
            new_input = solvers.Input(3)
            del new_input
            continue
        elif choice == 4:
            new_input = solvers.Input(4)
            del new_input
            continue
        elif choice == 5:
            new_input = solvers.Input(5)
            del new_input
            continue
        elif choice == 6:
            new_input = solvers.Input(6)
            del new_input
            continue
        elif choice == 7:
            print(color.BOLD + color.PURPLE, 'Удачи!', color.END)
            break
        else:
            print(color.BOLD + color.RED, "Неправильный ввод!", color.END)
            continue
    except TypeError:
        print(color.BOLD + color.RED, "Неправильный ввод!", color.END)
        continue
    except ValueError:
        continue