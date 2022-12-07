from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(root: Optional[TreeNode], result: List[int]) -> None:
            if root is None:
                return
            if low <= root.val <= high:
                result[0] += root.val
            if low <= root.val:
                dfs(root.left, result)
            if root.val <= high:
                dfs(root.right, result)

        result = [0]
        dfs(root, result)
        return result[0]
