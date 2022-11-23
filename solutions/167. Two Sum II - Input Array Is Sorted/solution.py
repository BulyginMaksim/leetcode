from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx in range(1, len(numbers)):
            cur_number = numbers[idx]
            found_idx = self.bin_search(numbers, idx, target - cur_number)
            if numbers[found_idx] + numbers[idx] == target:
                return [found_idx + 1, idx + 1]
        return [-1, -1]

    def bin_search(self, numbers: List[int], idx: int, target: int):
        left, right = -1, idx - 1
        while left < right - 1:
            mid = (left + right) // 2
            if numbers[mid] < target:
                left = mid
            else:
                right = mid
        return right
