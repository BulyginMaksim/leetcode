from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = dict()
        for task in tasks:
            if task not in freq:
                freq[task] = 0
            freq[task] += 1
        counter = 0
        for task, frequency in freq.items():
            if frequency == 1:
                return -1
            if frequency % 3 == 0:
                counter += frequency // 3
            else:
                counter += frequency // 3 + 1
        return counter
