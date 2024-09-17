from pydantic import BaseModel
from typing import List, Optional

class DataForGraph(BaseModel):
    name: str
    x: List[float]
    y: List[float]

class RequestModel(BaseModel):
    interpolationPoint: float
    x: List[float]
    y: List[float]

class ResponseModel(BaseModel):
    result: str
    graphs: List[DataForGraph]
