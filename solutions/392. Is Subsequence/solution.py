class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = len(s)
        first, second = len(s) - 1, len(t) - 1
        while first >= 0 and second >= 0:
            if s[first] == t[second]:
                counter -= 1
                first -= 1
                second -= 1
            else:
                second -= 1
        return not counter
