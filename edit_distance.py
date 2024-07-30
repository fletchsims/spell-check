import os
from typing import Sequence, TypeVar

import dotenv
import numpy as np

dotenv.load_dotenv()

T = TypeVar('T')


class EditDistance:
    def __init__(self):
        pass

    def compute_levenshtein_distance(self, s1: Sequence[T], s2: Sequence[T]) -> int:
        """Compute the Levenshtein distance between two strings.

        https://en.wikipedia.org/wiki/Levenshtein_distance
        """
        len_a = len(s1)
        len_b = len(s2)
        matrix = np.zeros((len_a + 1, len_b + 1), dtype=int)

        for i in range(len_a + 1):
            matrix[i][0] = i

        for j in range(len_b + 1):
            matrix[0][j] = j

        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,  # Deletion
                    matrix[i][j - 1] + 1,  # Insertion
                    matrix[i - 1][j - 1] + cost  # Substitution
                )
        return matrix[-1][-1]


    def compute_damerau_levenshtein_distance(self, s1: Sequence[T], s2: Sequence[T]) -> int:
        """Compute the Damerau-Levenshtein distance between two strings.

        https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
        """
        len_a = len(s1)
        len_b = len(s2)
        matrix = np.zeros((len_a + 1, len_b + 1), dtype=int)

        for i in range(len_a + 1):
            matrix[i][0] = i

        for j in range(len_b + 1):
            matrix[0][j] = j

        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,  # Deletion
                    matrix[i][j - 1] + 1,  # Insertion
                    matrix[i - 1][j - 1] + cost  # Substitution
                )
                if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                    matrix[i][j] = min(
                        matrix[i][j],
                        matrix[i - 2][j - 2] + cost  # Transposition
                    )
        return matrix[-1][-1]


edit = EditDistance()


def spell_check(word):
    with open(os.getenv('PATH_TO_DATA'), 'r') as f:
        lines = f.readlines()
    for line in lines:
        word_distance = edit.compute_damerau_levenshtein_distance('COLOMBIA', line.strip())


a = 'COLOMBIA'
b = 'COLUMBIA'
print(edit.compute_damerau_levenshtein_distance(a, b))

with open(os.getenv('PATH_TO_DATA'), 'r') as f:
    lines = f.readlines()

dictWordDist = []
wordIdx = 0

for line in lines:
    wordDistance = edit.compute_damerau_levenshtein_distance('COLUMBIA', line.strip())
    if wordDistance >= 10:
        wordDistance = 9
    dictWordDist.append(str(int(wordDistance)) + "-" + line.strip())
    wordIdx = wordIdx + 1

closestWords = []
wordDetails = []
currWordDist = 0
dictWordDist.sort()
# print(dictWordDist)
for i in range(3):
    currWordDist = dictWordDist[i]
    wordDetails = currWordDist.split("-")
    closestWords.append(wordDetails[1])

print(closestWords)
print(wordDetails)
