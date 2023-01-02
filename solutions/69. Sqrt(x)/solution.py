class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left, right = 0, x
        eps = 1e-2
        while right - left > eps:
            mid = (left + right) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return int(mid)
            if mid * mid < x:
                left = mid
            else:
                right = mid
        return int(left)
