from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cooldown, sell, hold = 0, 0, -float('inf')
        for price in prices:
            prev_cooldown, prev_sell, prev_hold = cooldown, sell, hold
            cooldown = max(prev_cooldown, prev_sell)
            sell = prev_hold + price
            hold = max(prev_hold, prev_cooldown - price)
        return max(sell, cooldown)
