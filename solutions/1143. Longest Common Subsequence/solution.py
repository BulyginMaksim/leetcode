class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n_rows, n_cols = len(text1), len(text2)
        dp = [[0 for _ in range(n_cols + 1)] for _ in range(n_rows + 1)]
        for idx in range(1, n_rows + 1):
            for jdx in range(1, n_cols + 1):
                if text1[idx - 1] == text2[jdx - 1]:
                    dp[idx][jdx] = 1 + dp[idx - 1][jdx - 1]
                else:
                    dp[idx][jdx] = max(
                        dp[idx - 1][jdx],
                        dp[idx][jdx - 1]
                    )
        return dp[-1][-1]
