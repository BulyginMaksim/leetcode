class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        first, second, third = 1, 1, 0
        for _ in range(n - 2):
            tmp = first + second + third
            third = second
            second = first
            first = tmp
        return first
