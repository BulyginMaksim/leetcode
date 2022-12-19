from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)
        used = [False] * n
        self.dfs(adj_list, source, used)
        return used[destination]

    def dfs(self, adj_list: List[List[int]], u: int, used: List[bool]):
        used[u] = True
        for v in adj_list[u]:
            if not used[v]:
                self.dfs(adj_list, v, used)
