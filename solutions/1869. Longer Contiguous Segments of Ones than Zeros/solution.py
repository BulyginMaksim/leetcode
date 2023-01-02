class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        cur_zeros = max_zeros = 0
        cur_ones = max_ones = 0
        for char in s:
            if char == '0':
                max_ones = max(cur_ones, max_ones)
                cur_ones = 0
                cur_zeros += 1
            else:
                max_zeros = max(cur_zeros, max_zeros)
                cur_zeros = 0
                cur_ones += 1
        return max(cur_zeros, max_zeros) < max(cur_ones, max_ones)
