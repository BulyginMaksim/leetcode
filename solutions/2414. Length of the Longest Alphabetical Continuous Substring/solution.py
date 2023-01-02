import string


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        char_ids = {char: idx for idx, char in enumerate(string.ascii_lowercase)}
        previous_char = s[0]
        current_len = 1
        max_len = 1
        for idx in range(1, len(s)):
            current_char = s[idx]
            if char_ids[current_char] - char_ids[previous_char] == 1:
                previous_char = current_char
                current_len += 1
                continue
            previous_char = current_char
            max_len = max(max_len, current_len)
            current_len = 1
        return max(max_len, current_len)
