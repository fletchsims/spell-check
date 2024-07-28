import numpy as np


def compute_dl_distance(a, b):
    """Compute the Damerau–Levenshtein distance between two strings.

    The distance is the sum of the number of insertions, deletions, substitutions, and transpositions.
    Cases:
    1. If both 'a' and 'b' are empty/same then the distance is 0
    2. If 'a' is empty then the distance is the length of 'b'
    3. If 'b' is empty then the distance is the length of 'a'
    """
    len_a = len(a)
    len_b = len(b)
    matrix = np.zeros((len_a + 1, len_b + 1))

    for i in range(len_a + 1):
        matrix[i][0] = i

    for j in range(len_b + 1):
        matrix[0][j] = j

    for i in range(1, len_a + 1):
        i: int
        j: int
        for j in range(1, len_b + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )

    return matrix[len_a][len_b]


a = 'cat'
b = 'cap'
print(compute_dl_distance(a, b))
