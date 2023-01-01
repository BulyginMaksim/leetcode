from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        matrix = [[0 for _ in range(c)] for _ in range(r)]
        idx, jdx = 0, 0
        for row in mat:
            for el in row:
                matrix[idx][jdx] = el
                if jdx == c - 1:
                    idx, jdx = idx + 1, 0
                else:
                    jdx += 1
        return matrix
