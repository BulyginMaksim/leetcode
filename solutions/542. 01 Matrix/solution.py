from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n_rows, n_cols = len(mat), len(mat[0])
        queue = []
        moves = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        for idx in range(n_rows):
            for jdx in range(n_cols):
                if mat[idx][jdx] == 0:
                    queue.append((idx, jdx))
                else:
                    mat[idx][jdx] = -1
        while queue:
            idx, jdx = queue.pop(0)
            for move in moves:
                idx_new, jdx_new = idx + move[0], jdx + move[1]
                if not 0 <= idx_new < n_rows or not 0 <= jdx_new < n_cols or mat[idx_new][jdx_new] != -1:
                    continue
                mat[idx_new][jdx_new] = mat[idx][jdx] + 1
                queue.append((idx_new, jdx_new))
        return mat
