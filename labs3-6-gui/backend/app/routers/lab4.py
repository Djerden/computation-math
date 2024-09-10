from fastapi import APIRouter, HTTPException
from app.models.lab4_models import *
from app.solvers.solver_lab4 import approximation

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

    # Преобразуем список объектов Pair в список списков [x, y]
    valid_pairs = [[pair.x, pair.y] for pair in pairs]

    # Вызов функции approximation для обработки данных
    try:
        results = approximation(valid_pairs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при аппроксимации данных: {str(e)}")

    # тестовый список пар x, y типа float
    # valid_pairs = [[0.4, 2.96], [0.8, 4.98], [1.2, 4.42], [1.6, 2.81], [2, 1.67], [2.4, 1.02], [2.8, 0.66], [3.2, 0.45]]

    # Вызов функции approximation для обработки данных
    results = approximation(valid_pairs)

    # Сделать проверку на ошибки, которые могут появиться в методе approximation

    response = create_response_model(valid_pairs, results)

    return response