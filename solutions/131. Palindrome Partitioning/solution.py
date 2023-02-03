from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(partitioning: List[str], start_idx: int):
            if start_idx == len(s):
                result.append(partitioning.copy())
                return
            for idx in range(start_idx, len(s)):
                if self.is_palindrome(s, start_idx, idx):
                    partitioning.append(s[start_idx: idx + 1])
                    backtrack(partitioning, idx + 1)
                    partitioning.pop()

        result = []
        backtrack([], start_idx=0)
        return result

    def is_palindrome(self, s: str, start: int, end: int):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
