from pydantic import BaseModel
from typing import List, Optional

class DataForGraphics(BaseModel):
    name: str
    method_x: List[float]
    method_y: List[float]
    exact_x: List[float]
    exact_y: List[float]

class RequestModel(BaseModel):
    y0: float
    x0: float
    xn: float
    h: float
    eps: float
    function: str

class ResponseModel(BaseModel):
    result: str
    graphics: List[DataForGraphics]