from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        frequencies = dict()
        max_frequency = 0
        min_length = float('inf')
        for idx, num in enumerate(nums):
            if num not in frequencies:
                frequencies[num] = [0, idx, idx]
            frequencies[num][0] += 1
            frequencies[num][2] = idx
            if frequencies[num][0] == max_frequency:
                min_length = min(min_length, frequencies[num][2] - frequencies[num][1] + 1)
            elif frequencies[num][0] > max_frequency:
                max_frequency = frequencies[num][0]
                min_length = frequencies[num][2] - frequencies[num][1] + 1
        return min_length
