from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current: List[int], start_idx: int):
            result.append(current.copy())
            for idx in range(start_idx, len(nums)):
                if idx > start_idx and nums[idx] == nums[idx - 1]:
                    continue
                current.append(nums[idx])
                backtrack(current, idx + 1)
                current.pop()
        nums.sort()
        result = []
        backtrack([], 0)
        return result
