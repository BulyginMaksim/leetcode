from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        return sum(self.is_valid(el, d, arr2) for el in arr1)

    def is_valid(self, el: int, d: int, arr2: List[int]) -> bool:
        l, r = 0, len(arr2)
        while l < r:
            mid = (l + r) // 2
            if abs(arr2[mid] - el) <= d:
                return False
            if arr2[mid] < el:
                l = mid + 1
            else:
                r = mid
        return True
