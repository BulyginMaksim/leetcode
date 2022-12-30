from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        result = []
        for num in nums:
            prefix_sum += num
            result.append(prefix_sum)
        return result
