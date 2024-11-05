import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import DNAResultPersister

client = TestClient(app)

def get_persisted_results(db_path: str):
    import sqlite3
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT is_mutant FROM dna_results')
        return cursor.fetchall()

def test_check_matrix_horizontal():
    response = client.post(
        "/check_matrix",
        json={"matrix": [["A", "A", "A", "A", "G", "A"],
                         ["C", "A", "G", "T", "G", "C"],
                         ["T", "T", "A", "T", "G", "T"],
                         ["A", "G", "A", "A", "G", "G"],
                         ["C", "C", "C", "C", "T", "A"],
                         ["T", "C", "A", "C", "T", "G"]]}
    )
    assert response.status_code == 200
    assert response.json() == {"is_mutant": True}
    results = get_persisted_results('dna_results.db')
    assert results[-1] == (True,)

def test_check_matrix_vertical():
    response = client.post(
        "/check_matrix",
        json={"matrix": [["A", "T", "G", "C", "G", "A"],
                         ["A", "A", "G", "T", "G", "C"],
                         ["A", "T", "A", "T", "G", "T"],
                         ["A", "G", "A", "A", "G", "G"],
                         ["C", "C", "C", "C", "T", "A"],
                         ["T", "C", "A", "C", "T", "G"]]}
    )
    assert response.status_code == 200
    assert response.json() == {"is_mutant": True}
    results = get_persisted_results('dna_results.db')
    assert results[-1] == (True,)

def test_check_matrix_diagonal_right():
    response = client.post(
        "/check_matrix",
        json={"matrix": [["A", "T", "G", "C", "G", "A"],
                         ["C", "A", "G", "T", "G", "C"],
                         ["T", "T", "A", "T", "G", "T"],
                         ["A", "G", "A", "A", "G", "G"],
                         ["C", "C", "C", "C", "A", "A"],
                         ["T", "C", "A", "C", "T", "A"]]}
    )
    assert response.status_code == 200
    assert response.json() == {"is_mutant": True}
    results = get_persisted_results('dna_results.db')
    assert results[-1] == (True,)

def test_check_matrix_diagonal_left():
    response = client.post(
        "/check_matrix",
        json={"matrix": [["A", "T", "G", "C", "G", "A"],
                         ["C", "A", "G", "T", "G", "C"],
                         ["T", "T", "A", "T", "G", "T"],
                         ["A", "G", "A", "A", "G", "G"],
                         ["C", "C", "C", "A", "T", "A"],
                         ["T", "C", "A", "C", "T", "G"]]}
    )
    assert response.status_code == 200
    assert response.json() == {"is_mutant": True}
    results = get_persisted_results('dna_results.db')
    assert results[-1] == (True,)