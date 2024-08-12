from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from starlette.middleware.cors import CORSMiddleware

import solver_lab3 as solver

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешите все источники (можете заменить на конкретные, если нужно)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешите все методы (GET, POST, и т.д.)
    allow_headers=["*"],  # Разрешите все заголовки
)

class Choice(BaseModel):
    equation: Optional[str] = None
    method: Optional[str] = None

class InputData(BaseModel):
    a: float
    b: float
    eps: float
    n: int

class RequestData(BaseModel):
    choice: Choice
    inputData: InputData

class ResponseData(BaseModel):
    answer: str

@app.post("/lab3", response_model=ResponseData)
async def process_data(request_data: RequestData):
    choice = request_data.choice
    input_data = request_data.inputData
    equation = 0
    match choice.equation:
        case "x^2":
            equation = 1
        case "sin(x)":
            equation = 25
        case "1/x":
            equation = 3
        case _:
            equation = 0
    if equation != 0:
        answer = ""
        match choice.method:
            case "rectangle-left":
                answer = solver.rectangle_method_left(equation, input_data.a, input_data.b, input_data.eps, input_data.n)
            case "rectangle-middle":
                answer = solver.rectangle_method_centre(equation, input_data.a, input_data.b, input_data.eps, input_data.n)
            case "rectangle-right":
                answer = solver.rectangle_method_right(equation, input_data.a, input_data.b, input_data.eps, input_data.n)
            case "trapezoidal":
                answer = solver.trapezoidal_method(equation, input_data.a, input_data.b, input_data.eps, input_data.n)
            case "simpson":
                answer = solver.simpson_method(equation, input_data.a, input_data.b, input_data.eps, input_data.n)
            case _:
                answer = "Invalid method"
        return ResponseData(answer=str(answer))

    # Логика обработки данных
    # Это просто пример, замените на вашу логику
    result = f"Processed equation {choice.equation} with method {choice.method} and input data {input_data}"

    return ResponseData(answer=result)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
