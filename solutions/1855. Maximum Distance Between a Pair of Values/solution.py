from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_diff = 0
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] > nums2[right]:
                left += 1
            else:
                max_diff = max(max_diff, right - left)
                right += 1
        return max_diff
