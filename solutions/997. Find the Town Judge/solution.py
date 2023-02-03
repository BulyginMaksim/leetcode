from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degrees = [[0, 0] for _ in range(n)]
        for edge in trust:
            person_from, person_to = edge
            degrees[person_from - 1][1] += 1
            degrees[person_to - 1][0] += 1
        counter = 0
        candidate = None
        for idx, degree in enumerate(degrees):
            if degree[0] == n - 1 and degree[1] == 0:
                candidate = idx + 1
                counter += 1
        return candidate if counter == 1 else -1
