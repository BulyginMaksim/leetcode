class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half_size = len(s) // 2
        vowels = {'a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U'}
        counter = 0
        for idx, char in enumerate(s):
            if char not in vowels:
                continue
            if idx >= half_size:
                counter -= 1
            else:
                counter += 1
        return not counter
