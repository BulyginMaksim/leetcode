class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mapping = {char: idx for idx, char in enumerate(order)}
        return ''.join(sorted(list(s), key=lambda x: mapping[x] if x in mapping else len(order)))
