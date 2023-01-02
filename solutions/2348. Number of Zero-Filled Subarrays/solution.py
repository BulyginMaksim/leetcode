from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        counter = 0
        result = 0
        for num in nums:
            if num == 0:
                counter += 1
                result += counter
            else:
                counter = 0
        return result
