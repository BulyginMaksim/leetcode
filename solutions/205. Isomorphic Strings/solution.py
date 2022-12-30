class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        first_in_second = dict()
        second_in_first = dict()
        for el1, el2 in zip(s, t):
            if el1 not in first_in_second:
                first_in_second[el1] = el2
            if el2 not in second_in_first:
                second_in_first[el2] = el1
            if first_in_second[el1] != el2 or second_in_first[el2] != el1:
                return False
        return True
