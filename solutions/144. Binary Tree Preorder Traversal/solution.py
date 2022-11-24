from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        self.dfs(root, traversal)
        return traversal

    def dfs(self, root: Optional[TreeNode], traversal: List[int]) -> None:
        if root is None:
            return
        traversal.append(root.val)
        self.dfs(root.left, traversal)
        self.dfs(root.right, traversal)
