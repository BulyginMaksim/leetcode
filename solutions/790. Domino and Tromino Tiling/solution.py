class Solution:
    def numTilings(self, n: int) -> int:
        mod_m = int(1e9) + 7
        if n <= 2:
            return n
        # dp[n] = dp[n - 1] + dp[n - 2] + 2 * (dp[n - 3] + ... + dp[0]) =
        # = dp[n - 1] + dp[n - 3] + dp[n - 2] + dp[n - 3] + 2 * (dp[n - 4] + ... + dp[0]) =
        # = dp[n - 1] + dp[n - 3] + dp[n - 1] = 2 * dp[n - 1] + dp[n - 3]
        last, second_last, third_last = 2, 1, 1
        for idx in range(3, n + 1):
            new_val = (2 * last + third_last) % mod_m
            third_last = second_last
            second_last = last
            last = new_val
        return last
