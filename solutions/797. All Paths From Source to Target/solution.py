from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        self.dfs(0, [0], paths, graph)
        return paths

    def dfs(self, vertex: int, path: List[int], paths: List[List[int]], graph: List[List[int]]):
        if vertex == len(graph) - 1:
            paths.append(path.copy())
            return
        for child_vertex in graph[vertex]:
            path.append(child_vertex)
            self.dfs(child_vertex, path, paths, graph)
            path.pop()
