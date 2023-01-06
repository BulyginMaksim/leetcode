from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is not None and root2 is not None:
            result = TreeNode((root1.val if root1 is not None else 0) + (root2.val if root2 is not None else 0))
            result.left = self.mergeTrees(root1.left, root2.left)
            result.right = self.mergeTrees(root1.right, root2.right)
            return result
        return root1 if root2 is None else root2
