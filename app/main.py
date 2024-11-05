from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.repositories.dna_repository import DNARepository
from app.services.mutant_service import is_mutant

app = FastAPI()
repo = DNARepository()

class DNARequest(BaseModel):
    dna: list[str]

@app.post("/mutant/")
async def mutant(dna_request: DNARequest):
    dna = dna_request.dna

    if is_mutant(dna):
        repo.save_result(dna, True)
        return {"message": "Mutant detected"}
    else:
        repo.save_result(dna, False)
        raise HTTPException(status_code=403, detail="Not a mutant")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)