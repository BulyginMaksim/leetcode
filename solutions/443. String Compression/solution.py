from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        char = chars[0]
        counter = 1
        idx_to_place = 0
        for idx in range(1, len(chars)):
            if chars[idx] == char:
                counter += 1
                continue
            idx_to_place = self.proceed_inserting(chars, char, counter, idx_to_place)
            counter = 1
            char = chars[idx]
        idx_to_place = self.proceed_inserting(chars, char, counter, idx_to_place)
        return idx_to_place

    def proceed_inserting(self, chars: List[str], char: str, counter: int, idx: int):
        chars[idx] = char
        idx += 1
        if counter != 1:
            for int_char in list(str(counter)):
                chars[idx] = int_char
                idx += 1
        return idx
