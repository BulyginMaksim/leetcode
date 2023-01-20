from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current_nums: List[int], start_idx: int):
            if len(current_nums) >= 2:
                result.append(current_nums.copy())
            used = set()
            for idx in range(start_idx, len(nums)):
                if (not current_nums or current_nums[-1] <= nums[idx]) and nums[idx] not in used:
                    used.add(nums[idx])  # in order to avoid duplicate subsequences in result
                    current_nums.append(nums[idx])
                    backtrack(current_nums, idx + 1)
                    current_nums.pop()

        result = []
        backtrack([], start_idx=0)
        return result
