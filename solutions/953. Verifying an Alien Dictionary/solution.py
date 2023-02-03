from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        chars_mapping = {char: idx for idx, char in enumerate(order)}
        for idx in range(1, len(words)):
            is_sorted = self.is_word_less(words[idx - 1], words[idx], chars_mapping)
            if not is_sorted:
                return False
        return True

    def is_word_less(self, word1: str, word2: str, chars_mapping: dict) -> bool:
        n_first, n_second = len(word1), len(word2)
        left, right = 0, 0
        while left < n_first and right < n_second:
            if chars_mapping[word1[left]] < chars_mapping[word2[right]]:
                return True
            elif chars_mapping[word1[left]] > chars_mapping[word2[right]]:
                return False
            left += 1
            right += 1
        return len(word1) <= len(word2)
