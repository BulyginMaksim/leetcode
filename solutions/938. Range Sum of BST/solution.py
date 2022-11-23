from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        return self.dfs(root, low, high)

    def dfs(self, node: TreeNode, low: int, high: int):
        if node.left is None and node.right is None:
            if low <= node.val <= high:
                return node.val
            return 0
        cur_sum = node.val if low <= node.val <= high else 0
        if node.left is not None:
            cur_sum += self.dfs(node.left, low, high)
        if node.right is not None:
            cur_sum += self.dfs(node.right, low, high)
        return cur_sum
