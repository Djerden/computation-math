from fastapi import APIRouter, HTTPException
from app.solvers.solver_lab6.solver_lab6 import *
from app.models.lab6_models import *

router = APIRouter()

@router.post("/lab6", response_model=ResponseModel)
async def process_data(request_data: RequestModel):

    y0 = request_data.y0
    x0 = request_data.x0
    xn = request_data.xn
    h = request_data.h
    eps = request_data.eps
    func = request_data.function

    result, graphics = solve(y0, x0, xn, h, eps, func)

    return ResponseModel(result=result, graphics=graphics)