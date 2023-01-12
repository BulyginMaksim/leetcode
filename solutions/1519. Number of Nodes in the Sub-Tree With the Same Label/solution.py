import string
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjency = [[] for _ in range(n)]
        for edge in edges:
            adjency[edge[0]].append(edge[1])
            adjency[edge[1]].append(edge[0])
        result = [0 for _ in range(n)]
        self.chars_mapping = {char: idx for idx, char in enumerate(string.ascii_lowercase)}
        self.n_chars = len(self.chars_mapping)
        self.dfs(0, result, adjency, labels)
        return result

    def dfs(self, vertex: int, result: List[int], adjency: List[List[int]], labels: str) -> List[int]:
        counter = [0 for _ in range(self.n_chars)]
        result[vertex] = 1
        counter[self.chars_mapping[labels[vertex]]] = 1
        for child in adjency[vertex]:
            if not result[child]:
                got_counter = self.dfs(child, result, adjency, labels)
                for idx in range(self.n_chars):
                    counter[idx] += got_counter[idx]
        result[vertex] = counter[self.chars_mapping[labels[vertex]]]
        return counter
