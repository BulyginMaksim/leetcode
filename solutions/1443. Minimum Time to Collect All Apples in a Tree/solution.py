from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjency = [[] for _ in range(n)]
        for edge in edges:
            adjency[edge[0]].append(edge[1])
            adjency[edge[1]].append(edge[0])
        result = self.dfs(adjency, hasApple, 0, -1)
        return max(result - 2, 0)  # since vertex 0 is counted twice when should not be

    def dfs(self, adjency: List[List[int]], hasApple: List[bool],
            node: int, parent_node: int) -> int:
        paths_doubled = 0
        for child_node in adjency[node]:
            if child_node != parent_node:
                paths_doubled += self.dfs(adjency, hasApple, child_node, node)
        return paths_doubled + 2 if hasApple[node] or paths_doubled else 0
