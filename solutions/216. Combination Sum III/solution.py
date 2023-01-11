from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(current: List[int], current_sum: int, start_num: int):
            if len(current) == k and current_sum == n:
                result.append(current.copy())
                return
            for num in range(start_num, 10):
                if current_sum + num > n:
                    continue
                current.append(num)
                backtrack(current, current_sum + num, num + 1)
                current.pop()

        result = []
        backtrack([], 0, 1)
        return result
