# tests/test_mutant_checker.py
import pytest
from app.services.mutant_service import is_mutant

def test_is_mutant_horizontal():
    dna = ["AAAAAG", "CAGTGC", "TTATGT", "AGAAGG", "CCCCAA", "TCACGT"]
    assert is_mutant(dna) == True

def test_is_mutant_vertical():
    dna = ["ATGCGA", "AAGTGC", "ATATGT", "AGAAGG", "CCCCAA", "TCACGT"]
    assert is_mutant(dna) == True

def test_is_mutant_diagonal_right():
    dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCAA", "TCACAA"]
    assert is_mutant(dna) == True

def test_is_mutant_diagonal_left():
    dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCTAA", "TCACGT"]
    assert is_mutant(dna) == True

def test_is_human():
    dna = ["ATGCGA",
           "CAGTGC",
           "TTATGT",
           "AGAACG",
           "CCCTTA",
           "TCACTG"]
    assert is_mutant(dna) == False

def test_is_human_no_mutant_sequences():
    dna = ["ATGCGA",
           "CAGTGC",
           "TTATGT",
           "AGACGG",
           "GCGTCA",
           "TCACTG"]
    assert is_mutant(dna) == False

def test_is_mutant_mixed_sequences():
    dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    assert is_mutant(dna) == True