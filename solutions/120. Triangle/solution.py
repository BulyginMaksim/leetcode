from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        row = triangle[-1]
        idx = n - 2
        while idx >= 0:
            i = 0
            while i < len(triangle[idx]):
                row[i] = triangle[idx][i] + min(row[i], row[i + 1])
                i += 1
            idx -= 1
        return row[0]
