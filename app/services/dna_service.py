from app.repositories.dna_repository import DNARepository
from app.mutant_checker import check_sequences

class DNAService:
    def __init__(self):
        self.dna_repository = DNARepository()

    def analyze(self, matrix):
        is_mutant = check_sequences(matrix)
        self.dna_repository.save_result(matrix, is_mutant)
        return is_mutant