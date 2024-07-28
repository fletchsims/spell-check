import numpy as np


def compute_dl_distance(a, b):
    """Compute the Damerau–Levenshtein distance between two strings."""
    len_a = len(a)
    len_b = len(b)
    matrix = np.zeros((len_a + 1, len_b + 1), dtype=int)

    for i in range(-1, len_a + 1):
        matrix[i][0] = i

    for j in range(-1, len_b + 1):
        matrix[0][j] = j

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )

    print(matrix)
    return matrix[-1][-1]


a = 'cat'
b = 'cap'
print(compute_dl_distance(a, b))
