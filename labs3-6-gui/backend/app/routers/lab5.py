from fastapi import APIRouter, HTTPException
from app.models.lab5_models import *
from app.solvers.solver_lab5 import *

router = APIRouter()



@router.post("/lab5")
async def process_data(request_data):
    pass