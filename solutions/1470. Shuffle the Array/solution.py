from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        half_size = len(nums) // 2
        for idx in range(half_size):
            result.append(nums[idx])
            result.append(nums[half_size + idx])
        return result
