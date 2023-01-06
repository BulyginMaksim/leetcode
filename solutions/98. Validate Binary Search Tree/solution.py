from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.dfs(root, -float('inf'), float('inf'))

    def dfs(self, node: Optional[TreeNode], left: int, right: int) -> bool:
        if node is None:
            return True
        left_tree = self.dfs(node.left, left, node.val)
        right_tree = self.dfs(node.right, node.val, right)
        is_good_node = left < node.val < right
        return left_tree and right_tree and is_good_node
