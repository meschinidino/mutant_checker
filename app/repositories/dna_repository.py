class DNARepository:
    def __init__(self):
        self.conn = sqlite3.connect('dna_results.db')
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS dna_results (
                    dna TEXT PRIMARY KEY,
                    is_mutant BOOLEAN
                )
            ''')

    def save_result(self, dna: list[str], is_mutant: bool):
        dna_str = ''.join(dna)
        with self.conn:
            self.conn.execute('''
                INSERT OR REPLACE INTO dna_results (dna, is_mutant)
                VALUES (?, ?)
            ''', (dna_str, is_mutant))

    def count_mutant_dna(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM dna_results WHERE is_mutant = 1')
        return cursor.fetchone()[0]

    def count_human_dna(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM dna_results WHERE is_mutant = 0')
        return cursor.fetchone()[0]