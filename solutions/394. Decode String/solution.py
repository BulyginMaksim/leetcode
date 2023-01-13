class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_value = 0
        cur_string = []
        for char in s:
            if char == '[':
                stack.append(cur_string)
                stack.append(cur_value)
                cur_string = []
                cur_value = 0
            elif char == ']':
                n_repeats = stack.pop()
                previous_string = stack.pop()
                cur_string = previous_string + n_repeats * cur_string
            elif char.isdigit():
                cur_value = cur_value * 10 + int(char)
            else:
                cur_string.append(char)
        return ''.join(cur_string)
    