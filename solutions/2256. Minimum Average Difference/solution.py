from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        suffix_sum = sum(nums)
        prefix_sum = 0
        n_nums = len(nums)
        res, min_idx = float('inf'), -1
        for idx, num in enumerate(nums):
            prefix_sum += nums[idx]
            suffix_sum -= nums[idx]
            left_val = prefix_sum // (idx + 1)
            right_val = 0 if idx == n_nums - 1 else suffix_sum // (n_nums - idx - 1)
            avg_diff = abs(left_val - right_val)
            if avg_diff < res:
                res = avg_diff
                min_idx = idx
        return min_idx
