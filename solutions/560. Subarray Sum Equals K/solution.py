from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefixes = {}
        counter = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefixes:
                counter += prefixes[prefix_sum - k]
            if prefix_sum == k:
                counter += 1
            if prefix_sum not in prefixes:
                prefixes[prefix_sum] = 0
            prefixes[prefix_sum] += 1
        return counter
