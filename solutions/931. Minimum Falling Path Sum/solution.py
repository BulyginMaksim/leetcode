from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n_rows, n_cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        # init with default state
        for jdx in range(n_cols):
            dp[n_rows - 1][jdx] = matrix[n_rows - 1][jdx]
        for idx in range(n_rows - 2, -1, -1):
            for jdx in range(n_cols):
                left_most = dp[idx + 1][jdx - 1] if 0 <= jdx - 1 else float('inf')
                mid_most = dp[idx + 1][jdx]
                right_most = dp[idx + 1][jdx + 1] if jdx + 1 < n_cols else float('inf')
                dp[idx][jdx] = matrix[idx][jdx] + min(left_most, mid_most, right_most)
        return min(dp[0])
