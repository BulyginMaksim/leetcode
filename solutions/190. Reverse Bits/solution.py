class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) + (n & 1)  # moving all bits to the right and adding last bit of n
            n = n >> 1
        return result
