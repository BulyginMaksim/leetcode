from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = float('inf')
        max_profit = 0
        for price in prices:
            if price < current_min:
                current_min = price
                continue
            if price - current_min > 0:
                max_profit = max(max_profit, price - current_min)
        return max_profit
