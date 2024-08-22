from fastapi import APIRouter, HTTPException
from app.models.lab3_models import *
from app.solvers.solver_lab3 import *

router = APIRouter()

@router.post("/lab3", response_model=ResponseData)
async def process_data(request_data: RequestData):
    choice = request_data.choice
    input_data = request_data.inputData
    equation = 0
    match choice.equation:
        case "x^2":
            equation = 1
        case "sin(x)":
            equation = 2
        case "1/x":
            equation = 3
        case _:
            equation = 0
    if equation != 0:
        answer = ""
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
                answer = "Invalid method"
        return ResponseData(answer=str(answer))

    # Логика обработки данных
    # Это просто пример, замените на вашу логику
    result = f"Processed equation {choice.equation} with method {choice.method} and input data {input_data}"

    return ResponseData(answer=result)