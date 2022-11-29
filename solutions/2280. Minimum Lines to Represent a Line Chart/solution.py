from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda pair: pair[0])
        n_days = len(stockPrices)
        if n_days <= 1:
            return 0
        if n_days == 2:
            return 1
        now_prices, now_days = self.get_pair(stockPrices[1], stockPrices[0])
        n_lines = 1
        for idx in range(2, n_days):
            diff_prices, diff_days = self.get_pair(
                stockPrices[idx],
                stockPrices[idx - 1]
            )
            if diff_prices != now_prices or diff_days != now_days:
                now_prices, now_days = diff_prices, diff_days
                n_lines += 1
        return n_lines

    def get_pair(self, pair1, pair2):
        diff_prices = pair1[1] - pair2[1]
        diff_days = pair1[0] - pair2[0]
        found_gcd = self.gcd(diff_prices, diff_days)
        if found_gcd != 1:
            diff_prices //= found_gcd
            diff_days //= found_gcd
        return diff_prices, diff_days

    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        while b:
            a, b = b, a % b
        return a
