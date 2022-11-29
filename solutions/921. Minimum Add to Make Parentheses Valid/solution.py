class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        to_open, to_close = 0, 0
        for char in s:
            if char == '(':
                to_close += 1
            else:
                if to_close > 0:
                    to_close -= 1
                else:
                    to_open += 1
        return to_open + to_close
