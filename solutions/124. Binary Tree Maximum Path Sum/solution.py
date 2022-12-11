from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            nonlocal max_val
            if node is None:
                return 0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            current_path = left_gain + right_gain + node.val
            max_val = max(max_val, current_path)

            return node.val + max(left_gain, right_gain)

        max_val = -float('inf')
        dfs(root)
        return max_val
