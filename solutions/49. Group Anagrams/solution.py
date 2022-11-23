from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for string in strs:
            current_string = tuple(sorted(list(string)))
            if current_string not in anagrams:
                anagrams[current_string] = [string]
            else:
                anagrams[current_string].append(string)
        return list(anagrams.values())
