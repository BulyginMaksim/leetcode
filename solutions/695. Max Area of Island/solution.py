from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.moves = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for idx in range(len(grid)):
            for jdx in range(len(grid[0])):
                if not visited[idx][jdx] and grid[idx][jdx] == 1:
                    max_area = max(max_area, self.dfs(grid, visited, idx, jdx))
        return max_area

    def dfs(self, grid: List[List[int]], visited: List[List[int]], idx: int, jdx: int) -> int:
        visited[idx][jdx] = 1
        area = 1
        for move in self.moves:
            idx_new, jdx_new = idx + move[0], jdx + move[1]
            if not (0 <= idx_new < len(grid) and 0 <= jdx_new < len(grid[0])):
                continue
            if not visited[idx_new][jdx_new] and grid[idx_new][jdx_new] == 1:
                area += self.dfs(grid, visited, idx_new, jdx_new)
        return area
