class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length, max_count = 0, 0
        counter = dict()
        for idx in range(len(s)):
            if s[idx] not in counter:
                counter[s[idx]] = 0
            counter[s[idx]] += 1
            max_count = max(max_count, counter[s[idx]])
            if max_length < k + max_count:
                max_length += 1
            else:
                counter[s[idx - max_length]] -= 1
        return max_length
