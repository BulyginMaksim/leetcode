from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2
        max_sum = 0
        for idx in range(n):
            max_sum += min(nums[2 * idx], nums[2 * idx + 1])
        return max_sum
