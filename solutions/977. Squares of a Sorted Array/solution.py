from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        first_positive = len(nums)
        for idx, num in enumerate(nums):
            if num >= 0:
                first_positive = idx
                break
        first_negative = first_positive - 1
        result = []
        while first_negative >= 0 and first_positive < len(nums):
            if abs(nums[first_negative]) < nums[first_positive]:
                result.append(nums[first_negative] * nums[first_negative])
                first_negative -= 1
            else:
                result.append(nums[first_positive] * nums[first_positive])
                first_positive += 1
        while first_negative >= 0:
            result.append(nums[first_negative] * nums[first_negative])
            first_negative -= 1
        while first_positive < len(nums):
            result.append(nums[first_positive] * nums[first_positive])
            first_positive += 1
        return result
