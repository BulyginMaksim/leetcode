from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        print(arr)
        for idx, num in enumerate(arr):
            found_idx = self.binary_search(arr, num * 2)
            if found_idx != idx and found_idx < len(arr) and num * 2 == arr[found_idx]:
                return True
        return False

    def binary_search(self, arr: List[int], target: int):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
