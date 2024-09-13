from app.solvers.solver_lab4.approximation_computing_util import evaluate_approximation

round_param = 5


def build_result(S, delta, R_squared, x_coord, y_coord, f, eps):
    # output_data = 'Мера отклонения = ' + str(S)+ '\n' + 'CKO = ' + str(delta) + '\n' + 'R^2 = ' + str(R_squared) + '\n' + evaluate_approximation(R_squared) + '\n' + "x_i: ", " , ".join(map(str, xs)) + '\n' + "y_i: ", " , ".join(map(str, ys)) +'\n'+ "f(x_i): ", " , ".join(map(str, f))  +'\n' + "eps_i: ", " , ".join(map(str, eps))
    # return output_data
    result = 'Мера отклонения = ' + str(S) + '\n'
    result += 'СКО = ' + str(delta) + '\n'
    result += 'Коэффициент детерминации R^2 = ' + str(R_squared) + '\n'
    result += evaluate_approximation(R_squared) + '\n'
    # result += "x_i: ", " , ".join(map(str, x_coord)) + '\n'
    # result += "y_i: ", " , ".join(map(str, y_coord)) + '\n'
    # result += "f(x_i): ", " , ".join(map(str, f)) + '\n'
    # result += "eps_i: ", " , ".join(map(str, eps)) + '\n'
    # result += 'x_i: '
    # for i in x_coord:
    #     result += str(round(i, round_param)) + ' '
    # result += '\n' + 'y_i: '
    # for i in y_coord:
    #     result += str(round(i, round_param)) + ' '
    result += 'fi(x_i): '
    c = 0
    for i in f:
        if c % 3 == 0:
            result += '\n   '
        c += 1
        result += str(round(i, round_param)) + ' '
    result += '\n' + 'eps_i: '
    c = 0
    for i in eps:
        if c % 3 == 0:
            result += '\n   '
        c += 1
        result += str(round(i, round_param)) + ' '
    result += '\n'
    # print(f'Мера отклонения = {S}')
    # print(f'СКО = {delta}')
    # print(f"Коэффициент детерминации R^2= {R_squared}")
    # print(evaluate_approximation(R_squared))
    # print("x_i: ", " , ".join(map(str, x_coord)))
    # print("y_i: ", " , ".join(map(str, y_coord)))
    # print("f(x_i): ", " , ".join(map(str, f)))
    # print("eps_i: ", " , ".join(map(str, eps)))
    return result
