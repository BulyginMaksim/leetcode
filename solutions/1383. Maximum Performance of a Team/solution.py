import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [(ef, sp) for sp, ef in zip(speed, efficiency)]
        engineers.sort(reverse=True)
        h = []
        cur_sum = 0
        result = 0
        for ef, sp in engineers:
            heapq.heappush(h, sp)
            cur_sum += sp
            if len(h) > k:
                cur_sum -= heapq.heappop(h)
            result = max(result, cur_sum * ef)
        return result % (10 ** 9 + 7)
