from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        if root.val == p.val or root.val == q.val:
            return root
        left_found, right_found = None, None
        if root.left:
            left_found = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right_found = self.lowestCommonAncestor(root.right, p, q)
        if left_found is not None and right_found is not None:
            return root
        elif left_found is None and right_found is not None:
            return right_found
        elif left_found is not None and right_found is None:
            return left_found
        return None
