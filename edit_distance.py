import numpy as np


def compute_levenshtein_distance(a, b):
    """Compute the Levenshtein distance between two strings."""
    len_a = len(a)
    len_b = len(b)
    matrix = np.zeros((len_a + 1, len_b + 1), dtype=int)

    for i in range(len_a + 1):
        matrix[i][0] = i

    for j in range(len_b + 1):
        matrix[0][j] = j

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,  # Deletion
                matrix[i][j - 1] + 1,  # Insertion
                matrix[i - 1][j - 1] + cost  # Substitution
            )

    print(matrix)
    return matrix[-1][-1]


def compute_damerau_levenshtein_distance(a, b):
    """Compute the Damerau-Levenshtein distance between two strings."""
    len_a = len(a)
    len_b = len(b)
    matrix = np.zeros((len_a + 1, len_b + 1), dtype=int)

    for i in range(len_a + 1):
        matrix[i][0] = i

    for j in range(len_b + 1):
        matrix[0][j] = j

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,      # Deletion
                matrix[i][j - 1] + 1,      # Insertion
                matrix[i - 1][j - 1] + cost  # Substitution
            )
            if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                matrix[i][j] = min(
                    matrix[i][j],
                    matrix[i - 2][j - 2] + cost  # Transposition
                )

    print(matrix)
    return matrix[-1][-1]


a = 'martha'
b = 'marhta'
print(compute_levenshtein_distance(a, b))
print(compute_damerau_levenshtein_distance(a, b))
