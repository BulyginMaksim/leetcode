from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.swap(nums, n - k, n)
        self.swap(nums, 0, n - k)
        self.swap(nums, 0, n)

    def swap(self, nums: List[int], left: int, right: int) -> None:
        right -= 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
