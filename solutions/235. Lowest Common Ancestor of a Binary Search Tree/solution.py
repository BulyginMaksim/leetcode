from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        while root:
            if root.val < min_val:
                root = root.right
            elif root.val > max_val:
                root = root.left
            else:
                return root
        return None
