class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            coint_stairs_sum = mid * (mid + 1) / 2
            if coint_stairs_sum > n:
                right = mid
            else:
                left = mid + 1
        return right - 1
