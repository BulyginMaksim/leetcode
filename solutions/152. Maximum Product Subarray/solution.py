from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_product, suffix_product = nums[0], nums[n - 1]
        max_prefix, max_suffix = prefix_product, suffix_product
        for idx in range(1, n):
            if prefix_product:
                prefix_product *= nums[idx]
            else:
                prefix_product = nums[idx]

            if suffix_product:
                suffix_product *= nums[n - idx - 1]
            else:
                suffix_product = nums[n - idx - 1]
            max_prefix = max(prefix_product, max_prefix)
            max_suffix = max(suffix_product, max_suffix)
        return max(max_prefix, max_suffix)
