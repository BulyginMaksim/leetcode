class Solution:
    def maxPower(self, s: str) -> int:
        max_pow = 1
        cur_pow = 1
        cur_char = s[0]
        for idx in range(1, len(s)):
            if s[idx] == cur_char:
                cur_pow += 1
            else:
                max_pow = max(cur_pow, max_pow)
                cur_pow = 1
                cur_char = s[idx]
        max_pow = max(cur_pow, max_pow)
        return max_pow
