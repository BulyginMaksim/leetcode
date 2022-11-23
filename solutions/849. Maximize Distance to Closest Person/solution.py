from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        begin = 0 if seats[0] else -1
        max_dist = 0
        for idx, num in enumerate(seats):
            if not num:
                continue
            # case when leftmost seat is not taken
            if begin == -1:
                current_dist = idx - begin - 1
                max_dist = max(max_dist, current_dist)
                begin = idx
            if begin == idx:
                continue
            current_dist = (idx - begin) // 2
            max_dist = max(max_dist, current_dist)
            begin = idx
        # case when rightmost seat is not taken
        if begin != len(seats) - 1:
            current_dist = len(seats) - begin - 1
            max_dist = max(max_dist, current_dist)
        return max_dist
