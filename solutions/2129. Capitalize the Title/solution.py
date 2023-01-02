from typing import List


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        current_word = []
        result = []
        for idx, char in enumerate(title):
            if char != ' ':
                current_word.append(char)
                continue
            self.proceed_word(current_word, result)
            current_word = []
            result.append(' ')
        self.proceed_word(current_word, result)
        return ''.join(result)

    def proceed_word(self, current_word: List[str], result: List[str]) -> None:
        all_in_lowercase = len(current_word) <= 2
        for jdx, word_char in enumerate(current_word):
            if all_in_lowercase or not all_in_lowercase and jdx:
                result.append(word_char.lower())
            else:
                result.append(word_char.upper())
