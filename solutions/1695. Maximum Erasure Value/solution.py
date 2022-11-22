import typing as tp


class Solution:
    def maximumUniqueSubarray(self, nums: tp.List[int]) -> int:
        current_set = set()
        current_sum = 0
        idx_start = 0
        max_sum = 0
        for idx, num in enumerate(nums):
            while num in current_set:
                current_set.remove(nums[idx_start])
                current_sum -= nums[idx_start]
                idx_start += 1
            current_set.add(num)
            current_sum += num
            max_sum = max(current_sum, max_sum)
        return max_sum
