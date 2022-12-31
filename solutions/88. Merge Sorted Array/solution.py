from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first, second = m - 1, n - 1
        first_to_place = len(nums1) - 1
        while first >= 0 and second >= 0:
            if nums1[first] <= nums2[second]:
                nums1[first_to_place] = nums2[second]
                second -= 1
            else:
                nums1[first_to_place] = nums1[first]
                first -= 1
            first_to_place -= 1

        while first >= 0:
            nums1[first_to_place] = nums1[first]
            first -= 1
            first_to_place -= 1
        while second >= 0:
            nums1[first_to_place] = nums2[second]
            second -= 1
            first_to_place -= 1
