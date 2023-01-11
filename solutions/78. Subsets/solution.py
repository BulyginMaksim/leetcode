from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current: List[int], start_idx: int, used: Set[int]):
            result.append(current.copy())
            for idx in range(start_idx, len(nums)):
                if idx in used:
                    continue
                current.append(nums[idx])
                used.add(idx)
                backtrack(current, idx + 1, used)
                used.remove(idx)
                current.pop()

        result = []
        backtrack([], 0, set())
        return result
