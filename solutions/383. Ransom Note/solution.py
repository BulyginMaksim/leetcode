class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = dict()
        for char in magazine:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        for char in ransomNote:
            if char not in d or not d[char]:
                return False
            d[char] -= 1
        return True
