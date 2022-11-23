from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        begin, end = intervals[0]
        result = []
        for idx in range(1, len(intervals)):
            current_begin, current_end = intervals[idx]
            if begin <= current_begin <= end <= current_end:
                end = current_end
                continue
            if begin <= current_begin <= current_end <= end:
                continue
            if end < current_end:
                result.append([begin, end])
                begin, end = current_begin, current_end
                continue
        result.append([begin, end])
        return result
