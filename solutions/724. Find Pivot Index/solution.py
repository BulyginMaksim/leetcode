from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = 0
        suffix_sum = sum(nums)
        for idx, num in enumerate(nums):
            suffix_sum -= num
            if suffix_sum == prefix_sum:
                return idx
            prefix_sum += num
        return -1
