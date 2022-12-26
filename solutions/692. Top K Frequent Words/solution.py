from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies = dict()
        for word in words:
            if word not in frequencies:
                frequencies[word] = 0
            frequencies[word] -= 1
        pairs = sorted(frequencies.items(), key=lambda pair: (pair[1], pair[0]))
        return [pair[0] for pair in pairs[:k]]
