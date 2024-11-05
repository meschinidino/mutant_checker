from fastapi import FastAPI
from app.dna_checker import DNAAnalyzer, DNASequenceChecker

app = FastAPI()

dna_checker = DNASequenceChecker()
dna_analyzer = DNAAnalyzer(dna_checker)

@app.post("/check_matrix")
async def check_matrix(matrix: dict):
    is_mutant = dna_analyzer.analyze(matrix["matrix"])
    return {"is_mutant": is_mutant}