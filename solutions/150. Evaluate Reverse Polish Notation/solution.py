from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.is_operation(token):
                first = stack.pop()
                second = stack.pop()
                new_value = self.proceed_operation(first, second, token)
                stack.append(new_value)
            else:
                stack.append(int(token))
        return stack[0]

    def is_operation(self, token: str):
        return token in ('+', '-', '*', '/')

    def proceed_operation(self, first: int, second: int, token: str) -> int:
        if token == '+':
            return first + second
        elif token == '-':
            return second - first
        elif token == '*':
            return second * first
        elif token == '/':
            return int(second / first)
