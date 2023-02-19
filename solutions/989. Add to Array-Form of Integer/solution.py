from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num1 = num
        num2 = str(k)
        first, second = len(num1) - 1, len(num2) - 1
        result = []
        quotient = 0
        while first >= 0 and second >= 0:
            res = num1[first] + int(num2[second]) + quotient
            quotient = res // 10
            result.append(res % 10)
            first -= 1
            second -= 1
        while first >= 0:
            res = num1[first] + quotient
            quotient = res // 10
            result.append(res % 10)
            first -= 1
        while second >= 0:
            res = int(num2[second]) + quotient
            quotient = res // 10
            result.append(res % 10)
            second -= 1
        if quotient:
            result.append(quotient)
        return result[::-1]
