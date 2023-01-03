from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid
            else:
                left = mid + 1
        idx = right - 1
        left, right = 0, len(matrix[0])
        while left < right:
            mid = (left + right) // 2
            if matrix[idx][mid] > target:
                right = mid
            else:
                left = mid + 1
        return matrix[idx][right - 1] == target
