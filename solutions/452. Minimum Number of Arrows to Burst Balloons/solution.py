from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        start, stop = points[0]
        counter = 1
        for point in points:
            # {} -- start, stop
            # [] -- cur_start, cur_stop
            cur_start, cur_stop = point
            if start <= cur_start <= cur_stop <= stop:  # case {...[...]...}
                stop = cur_stop
                continue
            if start <= cur_start <= stop <= cur_stop:  # case {...[...}...]
                start = cur_start
                continue
            if start <= stop < cur_start <= cur_stop:  # case {...}...[...]
                counter += 1
                start, stop = cur_start, cur_stop
        return counter
