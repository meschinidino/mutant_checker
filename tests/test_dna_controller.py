# tests/test_dna_controller.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_check_matrix_mutant():
    response = client.post(
        "/check_matrix",
        json={"matrix": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]}
    )
    assert response.status_code == 200
    assert response.json() == {"is_mutant": True}

def test_check_matrix_human():
    response = client.post(
        "/check_matrix",
        json={"matrix": ["ATGCGA",
                         "CAGTGC",
                         "TTATGT",
                         "AGAACG",
                         "CCCTTA",
                         "TCACTG"]}
    )
    assert response.status_code == 200
    assert response.json() == {"is_mutant": False}

def test_check_matrix_human_no_mutant_sequences():
    response = client.post(
        "/check_matrix",
        json={"matrix": ["ATGCGA",
                         "CAGTGC",
                         "TTATGT",
                         "AGACGG",
                         "GCGTCA",
                         "TCACTG"]}
    )
    assert response.status_code == 200
    assert response.json() == {"is_mutant": False}

def test_check_matrix_mixed_sequences():
    response = client.post(
        "/check_matrix",
        json={"matrix": ["ATGCGA",
                         "CAGTGC",
                         "TTATGT",
                         "AGAAGG",
                         "CCCCTA",
                         "TCACTG"]}
    )
    assert response.status_code == 200
    assert response.json() == {"is_mutant": True}