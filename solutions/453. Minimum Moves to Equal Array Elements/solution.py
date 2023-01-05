from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_value = min(nums)
        result = 0
        for num in nums:
            result += num - min_value
        return result
