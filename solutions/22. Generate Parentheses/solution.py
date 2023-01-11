from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current: List[str], n_opened: int, n_closed: int):
            if n_opened + n_closed == 2 * n:
                result.append(''.join(current))
                return
            if n_opened < n:
                current.append('(')
                backtrack(current, n_opened + 1, n_closed)
                current.pop()
            if n_closed < n_opened:
                current.append(')')
                backtrack(current, n_opened, n_closed + 1)
                current.pop()

        result = []
        backtrack([], 0, 0)
        return result
