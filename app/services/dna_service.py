from app.services.mutant_service import is_mutant

def check_dna(dna: list[str]) -> bool:
    return is_mutant(dna)