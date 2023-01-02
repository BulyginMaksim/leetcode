from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        path = dict()
        self.count_odd = 0
        self.count_paths = 0
        self.dfs(root, path)
        return self.count_paths

    def dfs(self, root: TreeNode, path: dict):
        if root.val not in path:
            path[root.val] = 0
        if path[root.val] % 2 == 1:
            self.count_odd -= 1
        else:
            self.count_odd += 1
        path[root.val] += 1
        if root.left is None and root.right is None:
            if self.count_odd <= 1:
                self.count_paths += 1
        if root.left is not None:
            self.dfs(root.left, path)
        if root.right is not None:
            self.dfs(root.right, path)
        if path[root.val] % 2 == 1:
            self.count_odd -= 1
        else:
            self.count_odd += 1
        path[root.val] -= 1
