from app.solvers.solver_lab4.solver_lab4 import *

coordinates = [[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], [0.25, 1, 2.25, 4, 6.25, 9, 12.25, 16, 20.25, 25]]

print(linear_result(coordinates))
print(squared_result(coordinates))
print(triple_result(coordinates))
print(power_result(coordinates))
print(exponential_result(coordinates))
print(logarithm_result(coordinates))
print(best_approx())
