from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = dict()
        for value in nums:
            if value not in d:
                d[value] = 0
            d[value] += 1
        ans = 0
        for num, counter in d.items():
            if num - 1 in d:
                ans = max(ans, d[num] + d[num - 1])
        return ans
