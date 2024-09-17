from fastapi import APIRouter, HTTPException
from app.models.lab3_models import *
from app.solvers.solver_lab3 import *

router = APIRouter()

@router.post("/lab3", response_model=ResponseData)
async def process_data(request_data: RequestData):
    choice = request_data.choice
    input_data = request_data.inputData
    equation = None
    match choice.equation:
        case "x^2":
            equation = 1
        case "sin(x)":
            equation = 2
        case "1/x":
            equation = 3
        case _:
            raise HTTPException(status_code=400, detail="Invalid equation type provided.")

    input_data.a = float(input_data.a)
    input_data.b = float(input_data.b)
    input_data.eps = float(input_data.eps)
    input_data.n = int(input_data.n)  # Если `n` — целое число, преобразуем в `int`

    answer = None
    match choice.method:
        case "rectangle-left":
            answer = rectangle_method_left(equation, input_data.a, input_data.b, input_data.eps, input_data.n)
        case "rectangle-middle":
            answer = rectangle_method_centre(equation, input_data.a, input_data.b, input_data.eps, input_data.n)
        case "rectangle-right":
            answer = rectangle_method_right(equation, input_data.a, input_data.b, input_data.eps, input_data.n)
        case "trapezoidal":
            answer = trapezoidal_method(equation, input_data.a, input_data.b, input_data.eps, input_data.n)
        case "simpson":
            answer = simpson_method(equation, input_data.a, input_data.b, input_data.eps, input_data.n)
        case _:
            raise HTTPException(status_code=400, detail="Invalid method type provided.")

    if not answer:
        raise HTTPException(status_code=500, detail="Calculation failed due to an unknown error.")

    return ResponseData(square=answer[0], parts=answer[1], inaccuracy=answer[2])