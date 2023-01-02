class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        counter = 0
        for idx in range(1, len(s)):
            if s[idx] == '0' and s[idx - 1] == '1':
                counter += 1
        if s[-1] == '1':
            counter += 1
        return counter == 1
