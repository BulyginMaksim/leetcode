from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        leftmost_position = n - 1
        for idx in range(n - 2, -1, -1):
            if idx + nums[idx] >= leftmost_position:
                leftmost_position = idx
        return not leftmost_position
