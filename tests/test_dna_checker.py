import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.repositories.dna_repository import DNARepository
client = TestClient(app)

def get_persisted_results(db_path: str):
    import sqlite3
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT is_mutant FROM dna_results')
        return cursor.fetchall()

def test_check_matrix_horizontal():
    response = client.post(
        "/mutant/",
        json={"dna": ["AAAAAG",
                      "CAGTGC",
                      "TTATGT",
                      "AGAAGG",
                      "CCCCAA",
                      "TCACGT"]}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Mutant detected"}
    results = get_persisted_results('dna_results.db')
    assert results[-1] == (True,)

def test_check_matrix_vertical():
    response = client.post(
        "/mutant/",
        json={"dna": ["ATGCGA",
                      "AAGTGC",
                      "ATATGT",
                      "AGAAGG",
                      "CCCCAA",
                      "TCACGT"]}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Mutant detected"}
    results = get_persisted_results('dna_results.db')
    assert results[-1] == (True,)

def test_check_matrix_diagonal_right():
    response = client.post(
        "/mutant/",
        json={"dna": ["ATGCGA",
                      "CAGTGC",
                      "TTATGT",
                      "AGAAGG",
                      "CCCCAA",
                      "TCACAA"]}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Mutant detected"}
    results = get_persisted_results('dna_results.db')
    assert results[-1] == (True,)

def test_check_matrix_diagonal_left():
    response = client.post(
        "/mutant/",
        json={"dna": ["ATGCGA",
                      "CAGTGC",
                      "TTATGT",
                      "AGAAGG",
                      "CCCTAA",
                      "TCACGT"]}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Mutant detected"}
    results = get_persisted_results('dna_results.db')
    assert results[-1] == (True,)