from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total, current_total = 0, 0
        for idx in range(len(gas)):
            total += gas[idx] - cost[idx]
            current_total += gas[idx] - cost[idx]
            if current_total < 0:
                start = idx + 1
                current_total = 0
        return -1 if total < 0 else start
