# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n + 1
        while left < right:
            mid = (left + right) // 2
            got = guess(mid)
            if got == 0:
                return mid
            elif got == -1:
                right = mid - 1
            else:
                left = mid + 1
        return left
