from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        for idx in range(1, n):
            result[idx] = result[idx - 1] * nums[idx - 1]
        suffix = 1
        for idx in range(n - 1, -1, -1):
            result[idx] *= suffix
            suffix *= nums[idx]
        return result
