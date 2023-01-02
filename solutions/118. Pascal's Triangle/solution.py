from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for idx in range(2, numRows):
            current_row = [1]
            for jdx in range(1, len(result[-1])):
                current_row.append(result[-1][jdx] + result[-1][jdx - 1])
            current_row.append(1)
            result.append(current_row)
        return result
