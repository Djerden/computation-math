from fastapi import APIRouter, HTTPException
from app.models.lab5_models import *
from app.solvers.solver_lab5.solver_lab5 import *
from app.solvers.solver_lab5.coordinates_data_util import *

from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

@router.post("/lab5", response_model=ResponseModel)
async def process_data(request_data: RequestModel):

    result = ""

    x, y = sort_coordinates([request_data.x, request_data.y])

    inter_point = request_data.interpolationPoint

    result, graphs = solve_interpolation(x, y, inter_point)

    return ResponseModel(result=result, graphs=graphs, interpolation_nodes=[x, y])