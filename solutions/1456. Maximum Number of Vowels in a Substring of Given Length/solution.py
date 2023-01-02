class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')
        vowels_counter = 0
        vowels_current = dict()
        for idx in range(k):
            if s[idx] in vowels:
                if s[idx] not in vowels_current:
                    vowels_current[s[idx]] = 0
                vowels_current[s[idx]] += 1
                vowels_counter += 1
        vowels_max = vowels_counter
        for idx in range(k, len(s)):
            if s[idx - k] in vowels:
                vowels_current[s[idx - k]] -= 1
                vowels_counter -= 1
            if s[idx] in vowels:
                if s[idx] not in vowels_current:
                    vowels_current[s[idx]] = 0
                vowels_current[s[idx]] += 1
                vowels_counter += 1
            vowels_max = max(vowels_counter, vowels_max)
        return vowels_max
