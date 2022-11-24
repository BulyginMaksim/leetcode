from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_zero = set()
        cols_zero = set()
        rows, cols = len(matrix), len(matrix[0])
        for idx in range(rows):
            for jdx in range(cols):
                if not matrix[idx][jdx]:
                    rows_zero.add(idx)
                    cols_zero.add(jdx)
        for idx in rows_zero:
            for jdx in range(cols):
                matrix[idx][jdx] = 0
        for jdx in cols_zero:
            for idx in range(rows):
                matrix[idx][jdx] = 0
