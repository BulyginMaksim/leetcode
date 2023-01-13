from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adjency = [[] for _ in range(len(s))]
        for node, parent_node in enumerate(parent):
            if parent_node >= 0:
                adjency[parent_node].append(node)
        result = [0]
        self.dfs(result, 0, adjency, s)
        return result[0]

    def dfs(self, result: List[int], node: int, adjency: List[List[int]], s: str):
        candidates = [0]
        for child_node in adjency[node]:
            child_max_path = self.dfs(result, child_node, adjency, s)
            if s[child_node] != s[node]:
                candidates.append(child_max_path)

        candidates = sorted(candidates, reverse=True)[:2]  # not very smart, we could get two maximums in O(n)
        result[0] = max(result[0],
                        sum(candidates) + 1)  # sum candidates is sum of two longest paths which go trough our node
        return max(candidates) + 1
