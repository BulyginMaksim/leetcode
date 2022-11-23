class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        begin = 0
        max_len = 0
        for idx, char in enumerate(s):
            if char not in seen:
                seen.add(char)
                continue
            max_len = max(max_len, len(seen))
            while char in seen:
                print(begin)
                seen.remove(s[begin])
                begin += 1
            seen.add(char)
        max_len = max(max_len, len(seen))
        return max_len
