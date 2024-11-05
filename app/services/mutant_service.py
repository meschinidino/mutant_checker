from app.mutant_checker import check_sequences

def is_mutant(dna: list[str]) -> bool:
    return check_sequences(dna)