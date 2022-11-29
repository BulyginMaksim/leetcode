class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
            1000: "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I",
            0: ""
        }
        mapping = {
            0: [0],
            1: [1],
            2: [1, 1],
            3: [1, 1, 1],
            4: [1, 5],
            5: [5],
            6: [5, 1],
            7: [5, 1, 1],
            8: [5, 1, 1, 1],
            9: [1, 10]
        }

        num_str = str(num)
        result, n = [], len(num_str)
        for i in range(n):
            val = int(num_str[n - i - 1])
            power = 10 ** i
            cur_str = []
            elements = mapping[val]
            for element in elements:
                cur_str.append(romans[element * power])
            result.append("".join(cur_str))
        return ''.join(result[::-1])
