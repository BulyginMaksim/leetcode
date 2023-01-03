class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = dict()
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        max_odd_val = 0
        for char, frequency in freq.items():
            if frequency % 2:
                max_odd_val = max(max_odd_val, frequency)
        seen_max_odd = False
        result_len = 0
        for char, frequency in freq.items():
            if not frequency % 2:
                result_len += frequency
                continue
            if frequency == max_odd_val and not seen_max_odd:
                result_len += frequency
                seen_max_odd = True
            else:
                result_len += frequency - 1
        return result_len
