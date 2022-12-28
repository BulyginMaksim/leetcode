import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        stones = []  # negative stone values, since in python heap by default is min-priority queue
        left_stones = 0
        for stone in piles:
            left_stones += stone
            stones.append(-stone)
        heapq.heapify(stones)
        for idx in range(k):
            stone = -heapq.heappop(stones)
            removed_stones = stone // 2
            if stone - removed_stones:
                heapq.heappush(stones, -(stone - removed_stones))
            left_stones -= removed_stones
        return left_stones
