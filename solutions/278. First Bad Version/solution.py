# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n + 1
        while left < right:
            mid = (left + right) // 2
            got = isBadVersion(mid)
            if got:
                right = mid
            else:
                left = mid + 1
        return left
