from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(combination, start):
            if k == len(combination):
                result.append(combination.copy())
                return
            for idx in range(start, n + 1):
                combination.append(idx)
                backtrack(combination, idx + 1)
                combination.pop()

        result = []
        backtrack([], 1)
        return result
