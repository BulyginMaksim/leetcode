from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                if target > nums[mid] or target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        if left == right and target != nums[left]:
            return -1
        return left
