def check_horizontal(matrix):
    total_rows = len(matrix)
    total_cols = len(matrix[0])
    occurrence_count = 0

    for row in range(total_rows):
        for col in range(total_cols - 3):
            if matrix[row][col] == matrix[row][col + 1] == matrix[row][col + 2] == matrix[row][col + 3]:
                occurrence_count += 1
                if occurrence_count >= 2:
                    return occurrence_count
    return occurrence_count

def check_vertical(matrix):
    total_rows = len(matrix)
    total_cols = len(matrix[0])
    occurrence_count = 0

    for row in range(total_rows - 3):
        for col in range(total_cols):
            if matrix[row][col] == matrix[row + 1][col] == matrix[row + 2][col] == matrix[row + 3][col]:
                occurrence_count += 1
                if occurrence_count >= 2:
                    return occurrence_count
    return occurrence_count

def check_diagonal(matrix):
    total_rows = len(matrix)
    total_cols = len(matrix[0])
    occurrence_count = 0

    for row in range(total_rows - 3):
        for col in range(total_cols - 3):
            if matrix[row][col] == matrix[row + 1][col + 1] == matrix[row + 2][col + 2] == matrix[row + 3][col + 3]:
                occurrence_count += 1
                if occurrence_count >= 2:
                    return occurrence_count

    for row in range(total_rows - 3):
        for col in range(3, total_cols):
            if matrix[row][col] == matrix[row + 1][col - 1] == matrix[row + 2][col - 2] == matrix[row + 3][col - 3]:
                occurrence_count += 1
                if occurrence_count >= 2:
                    return occurrence_count

    return occurrence_count

def check_sequences(matrix):
    horizontal_count = check_horizontal(matrix)
    vertical_count = check_vertical(matrix)
    diagonal_count = check_diagonal(matrix)

    total_occurrences = horizontal_count + vertical_count + diagonal_count
    return total_occurrences >= 2