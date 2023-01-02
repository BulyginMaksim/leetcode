from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue = [(root, 0)]
        prev_level = 0
        odd_blocks = []
        while queue:
            node, level = queue.pop(0)
            if level % 2 == 0 and prev_level % 2 == 1:
                left, right = 0, len(odd_blocks) - 1
                while left <= right:
                    odd_blocks[left].val, odd_blocks[right].val = odd_blocks[right].val, odd_blocks[left].val
                    left += 1
                    right -= 1
                odd_blocks = []
            if level % 2:
                odd_blocks.append(node)
            if node.left is not None and node.right is not None:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
            prev_level = level
        if odd_blocks:
            left, right = 0, len(odd_blocks) - 1
            while left <= right:
                odd_blocks[left].val, odd_blocks[right].val = odd_blocks[right].val, odd_blocks[left].val
                left += 1
                right -= 1
        return root
