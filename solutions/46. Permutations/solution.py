from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(combination, combination_set):
            if len(combination) == len(nums):
                result.append(combination.copy())
                return
            for num in nums:
                if num in combination_set:
                    continue
                combination.append(num)
                combination_set.add(num)
                backtrack(combination, combination_set)
                combination.pop()
                combination_set.remove(num)

        result = []
        backtrack([], set())
        return result
