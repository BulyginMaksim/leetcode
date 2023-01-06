from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        result = 0
        while result < len(costs) and coins > 0:
            if costs[result] > coins:
                break
            coins -= costs[result]
            result += 1
        return result
