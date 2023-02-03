from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(chars: List[str], cur_integers: List[str], ip_size: int, start_idx: int):
            # case: too big integers
            joined_chars = ''.join(chars)
            if len(chars) > 3 or (joined_chars and int(joined_chars) > 255):
                return
            # case: integer starting with '0'
            if len(chars) > 1 and chars[0] == '0':
                return
            if not chars and ip_size == len(s) and len(cur_integers) == 4:
                result.append('.'.join(cur_integers))
                return
            for idx in range(start_idx, len(s)):
                chars.append(s[idx])
                backtrack(chars, cur_integers, ip_size + 1, idx + 1)
                chars.pop()
            if chars:
                cur_integers.append(joined_chars)
                backtrack([], cur_integers, ip_size, start_idx)
                cur_integers.pop()

        result = []
        backtrack([], [], 0, 0)
        return result
