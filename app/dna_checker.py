from typing import List
from app.mutant_checker import check_sequences

class DNASequenceChecker:
    def check_sequence(self, matrix: List[List[str]]) -> bool:
        return check_sequences(matrix)

class DNAAnalyzer:
    def __init__(self, checker: DNASequenceChecker):
        self.checker = checker

    def analyze(self, matrix: List[List[str]]) -> bool:
        return self.checker.check_sequence(matrix)