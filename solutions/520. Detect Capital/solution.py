import string


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_letters = set(list(string.ascii_uppercase))
        not_capital_letters = set(list(string.ascii_lowercase))
        first_letter_is_capital = word[0] in capital_letters
        all_left_is_capital = True
        all_left_is_not_capital = True
        for idx in range(1, len(word)):
            if word[idx] in capital_letters:
                all_left_is_not_capital = False
            if word[idx] in not_capital_letters:
                all_left_is_capital = False
        all_capitals = first_letter_is_capital and all_left_is_capital
        all_not_capitals = not first_letter_is_capital and all_left_is_not_capital
        only_first_capital = first_letter_is_capital and all_left_is_not_capital
        return all_capitals or all_not_capitals or only_first_capital
