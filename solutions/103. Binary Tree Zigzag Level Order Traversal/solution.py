from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root, 0)]  # _ % 2 == 0 -> moving right
        stack_next = []
        result = []
        while stack or stack_next:
            if not stack:
                stack = stack_next
                stack_next = []
            node, level = stack.pop(-1)
            if node is None:
                continue
            while len(result) <= level:
                result.append([])
            result[level].append(node.val)
            # moving left at the moment
            if level % 2 == 1:
                stack_next.append((node.right, level + 1))
                stack_next.append((node.left, level + 1))
            # moving right at the moment
            else:
                stack_next.append((node.left, level + 1))
                stack_next.append((node.right, level + 1))
        return result
