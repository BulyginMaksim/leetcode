class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for idx in range(1, m):
            for jdx in range(1, n):
                dp[idx][jdx] = dp[idx - 1][jdx] + dp[idx][jdx - 1]
        return dp[-1][-1]
