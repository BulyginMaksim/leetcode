from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        left_space = sorted([cap - rock for cap, rock in zip(capacity, rocks)])
        number_filled_bags, idx = 0, 0
        while additionalRocks > 0 and idx < len(capacity):
            if left_space[idx] > additionalRocks:
                break
            additionalRocks -= left_space[idx]
            number_filled_bags += 1
            idx += 1
        return number_filled_bags

