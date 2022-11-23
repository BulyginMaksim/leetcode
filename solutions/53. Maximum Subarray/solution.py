from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        current_prefix_sum = 0
        max_subarray_sum = -float('inf')
        for num in nums:
            if current_prefix_sum < min_prefix_sum:
                min_prefix_sum = current_prefix_sum
            current_prefix_sum += num
            if max_subarray_sum < current_prefix_sum - min_prefix_sum:
                max_subarray_sum = current_prefix_sum - min_prefix_sum
        return max_subarray_sum

    def maxSubArraySecond(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]
        for idx in range(1, len(nums)):
            if dp[idx - 1] <= 0:
                dp[idx] = nums[idx]
            else:
                dp[idx] = dp[idx - 1] + nums[idx]
            max_sum = max(max_sum, dp[idx])
        return max_sum