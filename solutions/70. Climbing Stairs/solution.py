class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first, last = 1, 1
        for _ in range(n - 1):
            first, last = first + last, first
        return first
