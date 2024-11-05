import re

def is_mutant(dna: list[str]) -> bool:
    n = len(dna)
    sequences = []

    # Check horizontal sequences
    for row in dna:
        sequences.append(row)

    # Check vertical sequences
    for col in range(n):
        sequences.append("".join(dna[row][col] for row in range(n)))

    # Check diagonal (top-left to bottom-right) sequences
    for d in range(-n + 1, n):
        sequences.append("".join(dna[i][i - d] for i in range(max(d, 0), min(n + d, n))))

    # Check diagonal (top-right to bottom-left) sequences
    for d in range(-n + 1, n):
        sequences.append("".join(dna[i][n - 1 - i + d] for i in range(max(d, 0), min(n + d, n))))

    # Check for mutant sequences
    mutant_sequence = re.compile(r'(.)\1{3}')
    return any(mutant_sequence.search(seq) for seq in sequences)