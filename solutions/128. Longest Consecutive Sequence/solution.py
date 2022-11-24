from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        val_max = 0
        for el in s:
            if el - 1 not in s:
                cur_streak = 1
                while el + 1 in s:
                    cur_streak += 1
                    el += 1
                val_max = max(val_max, cur_streak)
        return val_max
