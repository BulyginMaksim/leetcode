from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.dfs(root, 0, targetSum)

    def dfs(self, node: Optional[TreeNode], current_sum: int, target_sum: int):
        if node.left is None and node.right is None:
            return current_sum + node.val == target_sum
        left_tree = self.dfs(node.left, current_sum + node.val, target_sum) if node.left is not None else False
        right_tree = self.dfs(node.right, current_sum + node.val, target_sum) if node.right is not None else False
        return left_tree or right_tree
