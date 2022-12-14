from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        side_view = []
        self.dfs(root, 0, side_view)
        return side_view

    def dfs(self, node: Optional[TreeNode], level: int, side_view: List[int]):
        if node is None:
            return
        while len(side_view) < level + 1:
            side_view.append(0)
        side_view[level] = node.val
        self.dfs(node.left, level + 1, side_view)
        self.dfs(node.right, level + 1, side_view)
