class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = dict()
        d2 = dict()
        for el1, el2 in zip(s, t):
            if el1 not in d1:
                d1[el1] = 1
            else:
                d1[el1] += 1
            if el2 not in d2:
                d2[el2] = 1
            else:
                d2[el2] += 1
        for key in d1:
            if key not in d2 or d1[key] != d2[key]:
                return False
        return True
