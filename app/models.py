import sqlite3
import logging

class DNAResultPersister:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS dna_results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        is_mutant BOOLEAN NOT NULL
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating table: {e}")

    def persist_result(self, is_mutant: bool):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO dna_results (is_mutant) VALUES (?)', (is_mutant,))
                conn.commit()
                logging.info(f"Persisted result: is_mutant={is_mutant}")
        except sqlite3.Error as e:
            logging.error(f"Error persisting result: {e}")