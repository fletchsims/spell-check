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
        len_s1 = len(s1)
        len_s2 = len(s2)
        # If s1 and s2 are the same then they are 100% (1) similar
        if s1 == s2:
            return 1
        # Calculate the match distance (i.e. the distance to check for matching characters)
        match_distance = floor((max(len_s1, len_s2) / 2) - 1)
        t = 0
        m = 0

        # Check for the number of matches. For every i char in s1 check to see if j char in s2 matches + match_distance
        for i in range(len_s1):
            start = max(0, i - match_distance)
            end = min(i + match_distance + 1, len_s2)
            for j in range(start, end):
                if s1[i] == s2[j]:
                    print(s1[i])
                    print(s2[j])
                    m += 1
        if m == 0:
            return 0
        j_sim = ((m / len_s1) + (m / len_s2) + ((m - t) / m)) / 3
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
