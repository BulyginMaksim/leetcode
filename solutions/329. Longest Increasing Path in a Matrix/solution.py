from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        dp = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        max_val = 0
        for idx in range(n_rows):
            for jdx in range(n_cols):
                # already seen
                if dp[idx][jdx]:
                    continue
                val = self.dfs(matrix, dp, idx, jdx)
                max_val = max(max_val, val)
        return max_val

    def dfs(self, matrix: List[List[int]],
            dp: List[List[int]], idx: int, jdx: int):
        if dp[idx][jdx]:
            return dp[idx][jdx]
        found_max = 0
        moves = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        for move in moves:
            i_add, j_add = move
            if not (0 <= idx + i_add < len(dp)) or not (0 <= jdx + j_add < len(dp[0])):
                continue
            if matrix[idx][jdx] < matrix[idx + i_add][jdx + j_add]:
                val = self.dfs(matrix, dp, idx + i_add, jdx + j_add)
                if val > found_max:
                    found_max = val
        dp[idx][jdx] = found_max + 1
        return dp[idx][jdx]
