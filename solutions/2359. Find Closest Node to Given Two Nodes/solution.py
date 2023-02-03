from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n_vertices = len(edges)
        adjency = [[] for _ in range(n_vertices)]
        for idx, vertex in enumerate(edges):
            if vertex != -1:
                adjency[idx].append(vertex)
        distances1 = [-1 for _ in range(n_vertices)]
        distances2 = [-1 for _ in range(n_vertices)]
        self.dfs(node1, 0, adjency, distances1)
        self.dfs(node2, 0, adjency, distances2)
        found_min = float('inf')
        for dist1, dist2 in zip(distances1, distances2):
            if dist1 != -1 and dist2 != -1:
                found_min = min(found_min, max(dist1, dist2))
        print(distances1)
        print(distances2)
        for vertex in range(n_vertices):
            if max(distances1[vertex], distances2[vertex]) == found_min:
                return vertex
        return -1

    def dfs(self, vertex: int, path_len: int, adjency: List[List[int]], distances: List[int]):
        distances[vertex] = path_len
        for child_vertex in adjency[vertex]:
            if distances[child_vertex] == -1:
                self.dfs(child_vertex, path_len + 1, adjency, distances)
