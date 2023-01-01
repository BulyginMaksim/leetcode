from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first = dict()
        second = dict()
        for el in nums1:
            if el not in first:
                first[el] = 0
            first[el] += 1
        for el in nums2:
            if el not in second:
                second[el] = 0
            second[el] += 1
        result = []
        for num, freq in first.items():
            if num not in second:
                continue
            for _ in range(min(freq, second[num])):
                result.append(num)
        return result
