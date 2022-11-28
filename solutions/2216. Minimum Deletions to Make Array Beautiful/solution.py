from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        # nums[i - 1] != nums[i] if i % 2 == 1
        for idx, num in enumerate(nums):
            if not stack or len(stack) % 2 == 0:
                stack.append(num)
                continue
            if stack[-1] != num:
                stack.append(num)
        if len(stack) % 2:
            stack.pop()
        return len(nums) - len(stack)
