from fastapi import APIRouter, HTTPException
from app.models.lab6_models import *
from app.solvers.solver_lab6 import *

router = APIRouter()



@router.post("/lab6")
async def process_data(request_data):
    pass