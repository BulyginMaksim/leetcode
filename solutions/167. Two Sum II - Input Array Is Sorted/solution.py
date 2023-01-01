from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx in range(1, len(numbers)):
            cur_number = numbers[idx]
            found_idx = self.bin_search(numbers, idx, target - cur_number)
            if found_idx != idx and numbers[found_idx] + numbers[idx] == target:
                return [found_idx + 1, idx + 1]
        return [-1, -1]

    def bin_search(self, numbers: List[int], idx: int, target: int) -> int:
        left, right = 0, idx
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
