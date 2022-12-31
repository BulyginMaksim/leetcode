class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left < right:
            mid = (left + right) // 2
            got = mid ** 2
            if got < num:
                left = mid + 1
            else:
                right = mid
        return left ** 2 == num
