from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(idx: int, cur_letter: List[str]):
            if idx == len(s):
                combinations.append(''.join(cur_letter))
                return
            element = s[idx]
            if element.isnumeric():
                cur_letter.append(element)
                backtrack(idx + 1, cur_letter)
                cur_letter.pop()
            else:
                cur_letter.append(element.lower())
                backtrack(idx + 1, cur_letter)
                cur_letter.pop()
                cur_letter.append(element.upper())
                backtrack(idx + 1, cur_letter)
                cur_letter.pop()

        combinations = []
        backtrack(0, [])
        return combinations
