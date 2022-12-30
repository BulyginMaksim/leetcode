from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.left_search(nums, target)
        right = self.right_search(nums, target)
        return [left, right]

    def left_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if 0 <= left < len(nums) and nums[left] == target else -1

    def right_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return right - 1 if 0 <= right - 1 < len(nums) and nums[right - 1] == target else -1
