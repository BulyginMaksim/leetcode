from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = float('inf')
        max_profit = 0
        for num in prices:
            if num < current_min:
                current_min = num
                continue
            if num - current_min > 0:
                max_profit += num - current_min
                current_min = num
        return max_profit
