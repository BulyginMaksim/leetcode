class Solution:
    def reverseWords(self, s: str) -> str:
        begin, end = 0, 0
        result = []
        for idx, char in enumerate(s):
            if char != ' ':
                end += 1
                continue
            end -= 1
            while begin <= end:
                result.append(s[end])
                end -= 1
            result.append(' ')
            begin, end = idx + 1, idx + 1
        if end <= len(s):
            end -= 1
            while begin <= end:
                result.append(s[end])
                end -= 1
        return ''.join(result)
