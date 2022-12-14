from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        adjacent_house, after_one_house = nums[0], 0
        for idx in range(1, len(nums)):
            current_house = max(after_one_house + nums[idx], adjacent_house)
            after_one_house = adjacent_house
            adjacent_house = current_house
        return adjacent_house
