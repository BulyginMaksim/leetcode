from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for idx in range(int(n / 2)):
            for jdx in range(n):
                matrix[idx][jdx], matrix[n - idx - 1][jdx] = matrix[n - idx - 1][jdx], matrix[idx][jdx]

        for idx in range(n):
            for jdx in range(idx + 1, n):
                matrix[idx][jdx], matrix[jdx][idx] = matrix[jdx][idx], matrix[idx][jdx]
