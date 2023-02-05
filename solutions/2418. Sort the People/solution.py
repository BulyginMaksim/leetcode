from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_heights = [(name, height) for name, height in zip(names, heights)]
        return [pair[0] for pair in sorted(names_heights, key=lambda pair: pair[1], reverse=True)]
