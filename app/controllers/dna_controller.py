# app/controllers/dna_controller.py
from fastapi import APIRouter
from app.services.dna_service import check_dna

router = APIRouter()

@router.post("/check_matrix")
async def check_matrix(matrix: dict):
    is_mutant_result = check_dna(matrix["matrix"])
    return {"is_mutant": is_mutant_result}