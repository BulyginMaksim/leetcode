from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        self.dfs(root, 1, levels)
        return levels

    def dfs(self, node: Optional[TreeNode], level: int, levels: List[List[int]]) -> None:
        if node is None:
            return
        if len(levels) < level:
            levels.append([])
        levels[level - 1].append(node.val)
        self.dfs(node.left, level + 1, levels)
        self.dfs(node.right, level + 1, levels)
