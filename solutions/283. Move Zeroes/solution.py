from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_to_place = 0
        for idx, num in enumerate(nums):
            if not num:
                continue
            nums[idx_to_place] = num
            idx_to_place += 1
        while idx_to_place < len(nums):
            nums[idx_to_place] = 0
            idx_to_place += 1
