from typing import List, Set, Tuple


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        max_path_len, start, end = self.get_max_path_and_start_end(grid)
        seen = set()
        self.counter = 0
        self.moves = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        self.dfs(start, seen, grid, end, max_path_len)
        return self.counter

    def dfs(self, pair: Tuple[int, int], seen: Set[Tuple[int, int]],
            grid: List[List[int]], end: Tuple[int, int], max_path_len: int) -> None:
        m, n = len(grid), len(grid[0])
        idx, jdx = pair
        seen.add(pair)
        if len(seen) == max_path_len and (idx, jdx) == end:
            self.counter += 1
        for move in self.moves:
            idx_new = idx + move[0]
            jdx_new = jdx + move[1]
            is_good_pair = 0 <= idx_new < m and 0 <= jdx_new < n
            is_good_cell = grid[idx][jdx] + 1
            is_not_seen_before = (idx_new, jdx_new) not in seen
            if is_good_pair and is_good_cell and is_not_seen_before:
                self.dfs((idx_new, jdx_new), seen, grid, end, max_path_len)
        seen.remove(pair)

    def get_max_path_and_start_end(self, grid: List[List[int]]) -> Tuple[int, Tuple[int, int], Tuple[int, int]]:
        m, n = len(grid), len(grid[0])
        counter = 0
        end = None
        start = None
        for idx in range(m):
            for jdx in range(n):
                if grid[idx][jdx] + 1:
                    counter += 1
                if grid[idx][jdx] == 2:
                    end = (idx, jdx)
                if grid[idx][jdx] == 1:
                    start = (idx, jdx)
        return counter, start, end
