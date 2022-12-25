from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sums = []
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            prefix_sums.append(prefix_sum)
        return [self.binary_search(prefix_sums, query) for query in queries]

    def binary_search(self, array: List[int], find: int):
        left, right = 0, len(array)
        while left < right:
            mid = (left + right) // 2
            if array[mid] <= find:
                left = mid + 1
            else:
                right = mid
        return left
