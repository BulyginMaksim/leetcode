from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.adjency = self.get_adjency_list(n, edges)
        self.dist, self.count = [0] * n, [1] * n
        self.postorder(0, -1)
        self.preorder(n, 0, -1)
        return self.dist

    def get_adjency_list(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjency = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            adjency[v].append(u)
            adjency[u].append(v)
        return adjency

    def postorder(self, vertex: int, parent: int):
        for child in self.adjency[vertex]:
            if child != parent:
                self.postorder(child, vertex)
                self.count[vertex] += self.count[child]
                self.dist[vertex] += self.dist[child] + self.count[child]

    def preorder(self, n: int, vertex: int, parent: int):
        for child in self.adjency[vertex]:
            if child != parent:
                self.dist[child] = n - self.count[child] + self.dist[vertex] - self.count[child]
                self.preorder(n, child, vertex)
