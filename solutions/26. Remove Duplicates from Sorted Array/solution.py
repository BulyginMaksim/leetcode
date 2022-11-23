from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx_to_place = 0
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx - 1]:
                continue
            nums[idx_to_place] = nums[idx - 1]
            idx_to_place += 1
        nums[idx_to_place] = nums[-1]
        idx_to_place += 1
        return idx_to_place
