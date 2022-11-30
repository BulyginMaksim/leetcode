from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = dict()
        for num in arr:
            if num not in occurences:
                occurences[num] = 0
            occurences[num] += 1
        unique_occurences = set()
        for num, occurence in occurences.items():
            unique_occurences.add(occurence)
        return len(occurences) == len(unique_occurences)
