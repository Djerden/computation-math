from pydantic import BaseModel
from typing import Optional

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
    square: float
    parts: float
    inaccuracy: float