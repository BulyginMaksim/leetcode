class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        val = 1
        while val ** 2 <= 10e4:
            squares.append(val ** 2)
            val += 1
        dp = [0] * (n + 1)
        dp[1] = 1
        for value in range(2, n + 1):
            got_min = float('inf')
            for square in squares:
                if value - square < 0:
                    break
                if dp[value - square] < got_min:
                    got_min = dp[value - square]
            dp[value] = got_min + 1
        return dp[-1]
