class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequencies = dict()
        for idx, char in enumerate(s):
            if char not in frequencies:
                frequencies[char] = [1, idx]
            else:
                frequencies[char][0] += 1
        found_idx = -1
        frequency_min = float('inf')
        for char, pair in frequencies.items():
            if pair[0] > 1 or pair[0] > frequency_min:
                continue
            if found_idx == -1 or pair[1] < found_idx:
                frequency_min, found_idx = pair
        return found_idx
