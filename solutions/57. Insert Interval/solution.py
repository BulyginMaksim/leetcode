from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        cur_start, cur_end = newInterval
        is_new_interval_placed = False
        for interval in intervals:
            # [] - current interval
            # {} - new interval
            cur_interval_before_new = interval[1] < cur_start  # [] ... {}
            cur_interval_after_new = cur_end < interval[0]  # {} ... []
            if cur_interval_before_new or cur_interval_after_new:
                if cur_interval_after_new and not is_new_interval_placed:
                    new_intervals.append([cur_start, cur_end])
                    is_new_interval_placed = True
                new_intervals.append(interval)
            else:
                cur_start = min(cur_start, interval[0])
                cur_end = max(cur_end, interval[1])
        if not is_new_interval_placed:
            new_intervals.append([cur_start, cur_end])
        return new_intervals
