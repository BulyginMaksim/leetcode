class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m = len(num1) - 1, len(num2) - 1
        remainder = 0
        result = []
        while n >= 0 and m >= 0:
            cur_sum = int(num1[n]) + int(num2[m]) + remainder
            result.append(str(cur_sum % 10))
            remainder = cur_sum // 10
            n -= 1
            m -= 1
        while n >= 0:
            cur_sum = int(num1[n]) + remainder
            result.append(str(cur_sum % 10))
            remainder = cur_sum // 10
            n -= 1
        while m >= 0:
            cur_sum = int(num2[m]) + remainder
            result.append(str(cur_sum % 10))
            remainder = cur_sum // 10
            m -= 1
        if remainder:
            result.append(str(remainder))
        return ''.join(result[::-1])
