from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, firsts, seconds = 0, 0, 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                firsts += 1
            else:
                seconds += 1
        for idx in range(len(nums)):
            if zeros:
                nums[idx] = 0
                zeros -= 1
            elif firsts:
                nums[idx] = 1
                firsts -= 1
            else:
                nums[idx] = 2
                seconds -= 1
