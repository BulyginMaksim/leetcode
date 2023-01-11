class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        first = []
        for char in s:
            if char != '#':
                first.append(char)
                continue
            if first:
                first.pop()
        second = []
        for char in t:
            if char != '#':
                second.append(char)
                continue
            if second:
                second.pop()
        if len(first) != len(second):
            return False
        for char1, char2 in zip(first, second):
            if char1 != char2:
                return False
        return True
