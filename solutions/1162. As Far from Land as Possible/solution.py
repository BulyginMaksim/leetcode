from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = []
        n_rows = len(grid)
        found_water = False
        found_land = False
        for idx in range(n_rows):
            for jdx in range(n_rows):
                if grid[idx][jdx] == 1:
                    queue.append((idx, jdx))
                    found_land = True
                else:
                    found_water = True
        if not found_water or not found_land:
            return -1
        dp = [[0 for _ in range(n_rows)] for _ in range(n_rows)]
        moves = [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0)
        ]
        while queue:
            pair = queue.pop(0)
            idx, jdx = pair
            for move in moves:
                if not (0 <= idx + move[0] < n_rows and 0 <= jdx + move[1] < n_rows):
                    continue
                if grid[idx + move[0]][jdx + move[1]]:
                    continue
                if dp[idx + move[0]][jdx + move[1]]:
                    continue
                dp[idx + move[0]][jdx + move[1]] = dp[idx][jdx] + 1
                queue.append((idx + move[0], jdx + move[1]))
        return max([max(row) for row in dp])
