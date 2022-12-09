from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.dfs(root, res, root.val, root.val)
        return res[0]

    def dfs(self, node: TreeNode, res: List[int], min_val: int, max_val: int):
        if node is None:
            return None
        max_diff = max(abs(node.val - min_val), abs(node.val - max_val))
        res[0] = max(res[0], max_diff)
        new_max = max(node.val, max_val)
        new_min = min(node.val, min_val)
        self.dfs(node.left, res, new_min, new_max)
        self.dfs(node.right, res, new_min, new_max)
