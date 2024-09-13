from pydantic import BaseModel
from typing import List, Optional

class Pair(BaseModel):
    x: float
    y: float

class Approximation(BaseModel):
    name: str
    description: str
    function: Optional[str] = None

class ResponseModel(BaseModel):
    pairs: List[List[float]]
    functions: List[Approximation]
    bestApprox: Optional[str] = None