from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n, sum_vals = len(nums), 0
        cnt_zeros, cnt_ones, res = 0, 0, 0
        for num in nums:
            sum_vals += num
            if num:
                cnt_zeros += 1
                cnt_ones += 1
            else:
                cnt_ones = cnt_zeros
                cnt_zeros = 0
            res = max(res, cnt_ones, cnt_zeros)
        if sum_vals == n:
            return n - 1
        return res
