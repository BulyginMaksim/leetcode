from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.all_sum, self.ans = self.dfs(root, get_sum=True), 0
        self.dfs(root, get_sum=False)
        return self.ans % (10 ** 9 + 7)

    def dfs(self, node: Optional[TreeNode], get_sum: bool = True) -> int:
        if node is None:
            return 0
        current_sum = self.dfs(node.left, get_sum) + self.dfs(node.right, get_sum) + node.val
        if not get_sum:
            self.ans = max(self.ans, current_sum * (self.all_sum - current_sum))
        return current_sum
