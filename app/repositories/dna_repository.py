import sqlite3

class DNARepository:
    def __init__(self, db_path='dna_results.db'):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS dna_results (
                    id INTEGER PRIMARY KEY,
                    matrix TEXT,
                    is_mutant BOOLEAN
                )
            ''')
            conn.commit()

    def save_result(self, matrix, is_mutant):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO dna_results (matrix, is_mutant)
                VALUES (?, ?)
            ''', (str(matrix), is_mutant))
            conn.commit()