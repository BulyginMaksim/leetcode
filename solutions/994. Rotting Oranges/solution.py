from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        visited = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        queue = []
        for idx in range(n_rows):
            for jdx in range(n_cols):
                if grid[idx][jdx] == 2:
                    queue.append((idx, jdx, 0))
                    visited[idx][jdx] = 1
        max_minutes = 0
        moves = [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0)
        ]
        while queue:
            idx, jdx, n_minutes = queue.pop(0)
            max_minutes = max(n_minutes, max_minutes)
            for move in moves:
                if not 0 <= idx + move[0] < n_rows or not 0 <= jdx + move[1] < n_cols:
                    continue
                if not visited[idx + move[0]][jdx + move[1]] and grid[idx + move[0]][jdx + move[1]] == 1:
                    queue.append((idx + move[0], jdx + move[1], n_minutes + 1))
                    visited[idx + move[0]][jdx + move[1]] = 1
        for idx in range(n_rows):
            for jdx in range(n_cols):
                if grid[idx][jdx] == 1 and not visited[idx][jdx]:
                    return -1
        return max_minutes
