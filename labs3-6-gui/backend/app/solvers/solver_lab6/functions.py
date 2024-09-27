import sympy as sp
import numpy as np


def function1(x, y):
    return x ** 2 - 2 * y


def function2(x, y):
    # return y + sp.cos(x)
    return y + (1 + x) * y * y


def function3(x, y):
    #return 2 * x - 3 * y
    return  2 * x - 3 * y