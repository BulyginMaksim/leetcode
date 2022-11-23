class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
                continue
            if not len(stack) or not self.is_matching_brackets(stack[-1], char):
                return False
            stack.pop()
        return not len(stack)

    def is_matching_brackets(self, left: str, right: str) -> bool:
        if right == ']':
            return left == '['
        if right == '}':
            return left == '{'
        if right == ')':
            return left == '('
