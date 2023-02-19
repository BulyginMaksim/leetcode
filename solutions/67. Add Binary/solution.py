class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        first, second = len(a) - 1, len(b) - 1
        quotient = 0
        while first >= 0 and second >= 0:
            current = int(a[first]) + int(b[second]) + quotient
            if current % 2 == 0:
                result.append('0')
                quotient = current // 2
            else:
                result.append('1')
                quotient = current // 2
            first -= 1
            second -= 1
        print(result)
        while first >= 0:
            current = int(a[first]) + quotient
            if current % 2 == 0:
                result.append('0')
                quotient = current // 2
            else:
                result.append('1')
                quotient = current // 2
            first -= 1
        while second >= 0:
            current = int(b[second]) + quotient
            if current % 2 == 0:
                result.append('0')
                quotient = current // 2
            else:
                result.append('1')
                quotient = current // 2
            second -= 1
        if quotient:
            result.append('1')
        return ''.join(result[::-1])
