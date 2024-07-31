from math import floor
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

    def compute_hamming_distance(self, s1: Sequence[T], s2: Sequence[T]) -> int:
        """Compute the Hamming Distance between two strings.

        https://en.wikipedia.org/wiki/Hamming_distance
        """
        if len(s1) != len(s2):
            raise ValueError("Strings must have equal length")
        distance = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                distance += 1
        return distance

    def compute_jaro_similarity(self, s1: Sequence[T], s2: Sequence[T]) -> int:
        """Compute Jaro Similarity between two strings.

        https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance
        """
        if len(s1) != len(s2):
            raise ValueError("Strings must have equal length.")
        if s1 == s2:
            return 1

        max_distance = floor((max(len(s1), len(s2)) / 2) - 1)
        m = 0
        for i in range(len(s1)):
            for j in range(max(0, i - max_distance), min(len(s2)))
        return m



    def compute_jaro_winkler_similarity(self, s1: Sequence[T], s2: Sequence[T]) -> int:
        """Compute Jaro Winkler Similarity between two strings.

        https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance
        """
        pass


# edit = EditDistance()
# print(edit.compute_jaro_similarity("abcd", "abc"))
#
#
# def spell_check(word):
#     with open(os.getenv('PATH_TO_DATA'), 'r') as f:
#         lines = f.readlines()
#     for line in lines:
#         word_distance = edit.compute_damerau_levenshtein_distance('COLOMBIA', line.strip())
#
#
# a = 'COLOMBIA'
# b = 'COLUMBIA'
# print(edit.compute_damerau_levenshtein_distance(a, b))
#
# with open(os.getenv('PATH_TO_DATA'), 'r') as f:
#     lines = f.readlines()
#
# dictWordDist = []
# wordIdx = 0
#
# for line in lines:
#     wordDistance = edit.compute_damerau_levenshtein_distance('UNITED KINDOM', line.strip())
#     if wordDistance >= 10:
#         wordDistance = 9
#     dictWordDist.append(str(int(wordDistance)) + "-" + line.strip())
#     wordIdx = wordIdx + 1
#
# closestWords = []
# wordDetails = []
# currWordDist = 0
# dictWordDist.sort()
# print(dictWordDist)
# for i in range(3):
#     currWordDist = dictWordDist[i]
#     wordDetails = currWordDist.split("-")
#     closestWords.append(wordDetails[1])
#
# print(closestWords)
# print(wordDetails)
