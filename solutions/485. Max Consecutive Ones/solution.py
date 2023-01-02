from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_len = nums[0]
        max_len = current_len
        for idx in range(1, len(nums)):
            if nums[idx] == 0:
                max_len = max(current_len, max_len)
                current_len = 0
                continue
            current_len += 1
        return max(current_len, max_len)
