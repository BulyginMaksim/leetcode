from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        cur_vals = []
        return self.dfs(root, cur_vals)

    def dfs(self, root: TreeNode, cur_vals: List[str]):
        cur_vals.append(str(root.val))
        if root.left is None and root.right is None:
            path = int(''.join(cur_vals))
            cur_vals.pop()
            return path
        if root.left is None and root.right is not None:
            path = self.dfs(root.right, cur_vals)
            cur_vals.pop()
            return path
        if root.left is not None and root.right is None:
            path = self.dfs(root.left, cur_vals)
            cur_vals.pop()
            return path
        path = self.dfs(root.left, cur_vals) + self.dfs(root.right, cur_vals)
        cur_vals.pop()
        return path
