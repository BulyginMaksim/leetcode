from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for idx, element in enumerate(nums):
            if target - element in seen:
                return [seen[target - element], idx]
            seen[element] = idx
        return [-1, -1]
