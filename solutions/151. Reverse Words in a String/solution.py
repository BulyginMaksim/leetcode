class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = []
        begin = len(s) - 1
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] != ' ':
                continue
            if idx == begin:
                begin -= 1
                continue
            jdx = idx + 1
            while jdx <= begin:
                splitted.append(s[jdx])
                jdx += 1
            splitted.append(' ')
            begin = idx - 1
        if begin == -1 and splitted:
            splitted.pop()
        else:
            jdx = 0
            while jdx <= begin:
                splitted.append(s[jdx])
                jdx += 1
        return ''.join(splitted)
