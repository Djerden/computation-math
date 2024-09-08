from fastapi import APIRouter, HTTPException
from app.models.lab4_models import *
from app.solvers.solver_lab4 import approximation

from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Модель для линейной аппроксимации
class LinearApproximationResult(BaseModel):
    standard_deviation: float           # Стандартное отклонение
    s: float                            # S - мера отклонения (сумма квадратов отклонений)
    approximating_function: str         # Линейная аппроксимирующая функция
    p1_x: List[float]                   # Вычисленные значения полинома
    ei: List[float]                     # Погрешности (разница между знач. аппроксимирующей функции и заданных y)
    r: float                            # Коэффициент корреляции Пирсона
    p_i: List[float]                    # Дополнительные значения, если есть (например, p_i)
    a: float                            # Коэффициент a
    b: float                            # Коэффициент b

# Квадратичная аппроксимация
class SquareApproximationResult(BaseModel):
    standard_deviation: float
    s: float
    approximating_function: str
    p2_x: List[float]
    ei: List[float]
    p_i: List[float]
    a0: float
    a1: float
    a2: float

# Кубическая аппроксимация
class CubicApproximationResult(BaseModel):
    standard_deviation: float
    s: float
    approximating_function: str
    p2_x: List[float]
    ei: List[float]
    a0: float
    a1: float
    a2: float
    a3: float

# Экспоненциальная аппроксимация
class ExponentialApproximationResult(BaseModel):
    standard_deviation: float
    s: float
    approximating_function: str
    p_x: List[float]
    ei: List[float]
    r: float
    p_i: List[float]
    a: float
    b: float

# Логарифмическая аппроксимация
class LogarithmicApproximationResult(BaseModel):
    standard_deviation: float
    s: float
    approximating_function: str
    p_x: List[float]
    ei: List[float]
    r: float
    p_i: List[float]
    a: float
    b: float

# Степенная аппроксимация
class PowerApproximationResult(BaseModel):
    standard_deviation: float
    s: float
    approximating_function: str
    p_x: List[float]
    ei: List[float]
    r: float
    p_i: List[float]
    a: float
    b: float

# Ответ
class ResponseModel(BaseModel):
    linear: LinearApproximationResult
    square: SquareApproximationResult
    cubic: CubicApproximationResult
    exp: ExponentialApproximationResult
    logarithm: LogarithmicApproximationResult
    power: PowerApproximationResult


# Функция записи данных в модель ResponseModel
def create_response_model(results):
    return ResponseModel(
        linear=LinearApproximationResult(
            standard_deviation=results[0][0],
            s=results[0][1],
            approximating_function=results[0][2],
            p1_x=results[0][3],
            ei=results[0][4],
            r=results[0][5],
            p_i=results[0][6],
            a=results[0][7],
            b=results[0][8]
        ),
        square=SquareApproximationResult(
            standard_deviation=results[1][0],
            s=results[1][1],
            approximating_function=results[1][2],
            p2_x=results[1][3],
            ei=results[1][4],
            p_i=results[1][5],
            a0=results[1][6],
            a1=results[1][7],
            a2=results[1][8]
        ),
        cubic=CubicApproximationResult(
            standard_deviation=results[2][0],
            s=results[2][1],
            approximating_function=results[2][2],
            p2_x=results[2][3],
            ei=results[2][4],
            a0=results[2][5],
            a1=results[2][6],
            a2=results[2][7],
            a3=results[2][8]
        ),
        exp=ExponentialApproximationResult(
            standard_deviation=results[3][0],
            s=results[3][1],
            approximating_function=results[3][2],
            p_x=results[3][3],
            ei=results[3][4],
            r=results[3][5],
            p_i=results[3][6],
            a=results[3][7],
            b=results[3][8]
        ),
        logarithm=LogarithmicApproximationResult(
            standard_deviation=results[4][0],
            s=results[4][1],
            approximating_function=results[4][2],
            p_x=results[4][3],
            ei=results[4][4],
            r=results[4][5],
            p_i=results[4][6],
            a=results[4][7],
            b=results[4][8]
        ),
        power=PowerApproximationResult(
            standard_deviation=results[5][0],
            s=results[5][1],
            approximating_function=results[5][2],
            p_x=results[5][3],
            ei=results[5][4],
            r=results[5][5],
            p_i=results[5][6],
            a=results[5][7],
            b=results[5][8]
        )
    )
@router.post("/lab4", response_model=ResponseModel)
async def process_data():

    # Добавить чтение body запроса
    # Добавить валидацию полученного массива пар x, y

    # тестовый список пар x, y типа float
    valid_pairs = [[0.4, 2.96], [0.8, 4.98], [1.2, 4.42], [1.6, 2.81], [2, 1.67], [2.4, 1.02], [2.8, 0.66], [3.2, 0.45]]

    # Вызов функции approximation для обработки данных
    results = approximation(valid_pairs)

    # Сделать проверку на ошибки, которые могут появиться в методе approximation

    response = create_response_model(results)

    return response