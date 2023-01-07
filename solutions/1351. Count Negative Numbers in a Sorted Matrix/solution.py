from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        idx, jdx = 0, len(grid[0]) - 1
        counter = 0
        while jdx >= 0:
            while grid[idx][jdx] >= 0 and idx < len(grid) - 1:
                idx += 1
            counter += len(grid) - idx if grid[idx][jdx] < 0 else 0
            jdx -= 1
        return counter
