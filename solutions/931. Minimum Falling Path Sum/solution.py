from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n_rows, n_cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        # iterate from bottom to top to not do overcalculations
        for idx in range(n_rows - 1, -1, -1):
            for jdx in range(n_cols - 1, -1, -1):
                self.dfs(matrix, dp, idx, jdx)
        return min(dp[0])

    def dfs(self, matrix: List[List[int]], dp: List[List[int]],
            idx: int, jdx: int) -> int:
        if dp[idx][jdx]:
            return dp[idx][jdx]
        # only special moves from the task
        moves = (
            (1, -1),
            (1, 0),
            (1, 1)
        )
        dp[idx][jdx] = matrix[idx][jdx]
        min_path_found = None
        for move in moves:
            i, j = move
            if not self.is_good_idx(idx + i, jdx + j, matrix):
                continue
            got_path = self.dfs(matrix, dp, idx + i, jdx + j)
            if min_path_found is None or got_path < min_path_found:
                min_path_found = got_path
        if min_path_found is None:
            min_path_found = 0
        dp[idx][jdx] += min_path_found
        return dp[idx][jdx]

    def is_good_idx(self, idx: int, jdx: int, matrix: List[List[int]]) -> bool:
        idx_is_good = 0 <= idx < len(matrix)
        jdx_is_good = 0 <= jdx < len(matrix[0])
        return idx_is_good and jdx_is_good
