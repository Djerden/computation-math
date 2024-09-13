from fastapi import APIRouter, HTTPException
from app.models.lab4_models import *
from app.solvers.solver_lab4.solver_lab4 import *

from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()


@router.post("/lab4", response_model=ResponseModel)
async def process_data(pairs: List[Pair]):

    # Добавить чтение body запроса
    # Добавить валидацию полученного массива пар x, y

    # Валидация на количество пар
    if len(pairs) < 8 or len(pairs) > 12:
        raise HTTPException(status_code=400, detail="Количество валидных пар должно быть от 8 до 12.")

    # Преобразование pairs в вид [[x_coordinates], [y_coordinates]]
    x_coordinates = [pair.x for pair in pairs]  # Список всех координат x
    y_coordinates = [pair.y for pair in pairs]  # Список всех координат y
    coordinates = [x_coordinates, y_coordinates]

    try:
        linear = linear_result(coordinates)
        squared = squared_result(coordinates)
        triple = triple_result(coordinates)
        power = power_result(coordinates)
        exponential = exponential_result(coordinates)
        logarithm = logarithm_result(coordinates)
        bestAprox = best_approx()

    except Exception as e:
        raise HTTPException(status_code=500, detail="Возникла ошибка во время вычисления")

    # Преобразование списка объектов Pair в список списков
    coordinates_for_response = [[pair.x, pair.y] for pair in pairs]

    return ResponseModel(
        pairs=coordinates_for_response,
        functions=[linear, squared, triple, power, exponential, logarithm],
        bestAprox=bestAprox
    )