from fastapi import APIRouter
from app.services.dna_service import DNAService

router = APIRouter()
dna_service = DNAService()

@router.post("/check_matrix")
async def check_matrix(matrix: dict):
    is_mutant = dna_service.analyze(matrix["matrix"])
    return {"is_mutant": is_mutant}