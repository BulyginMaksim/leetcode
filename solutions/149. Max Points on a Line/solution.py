from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = 1
        n = len(points)
        for idx in range(n - 1):
            current_result = 1
            current_dict = dict()
            for jdx in range(idx + 1, n):
                intercept, coeff = self.get_line(points[idx], points[jdx])
                if (intercept, coeff) not in current_dict:
                    current_dict[(intercept, coeff)] = 1
                current_dict[(intercept, coeff)] += 1
                current_result = max(current_result, current_dict[(intercept, coeff)])
            # print(current_dict)
            result = max(current_result, result)
        return result

    def get_line(self, point1: List[int], point2: List[int]):
        x1, y1 = point1
        x2, y2 = point2
        if not x2 - x1:
            return 0, float('inf')
        coeff = (y2 - y1) / (x2 - x1)
        intercept = y1 - x1 * coeff
        return intercept, coeff
