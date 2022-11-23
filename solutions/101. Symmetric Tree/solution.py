from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None or root.left is None and root.right is None:
            return True
        if root.left is not None and root.right is not None:
            return self.is_symmetric_trees(root.left, root.right)
        return False

    def is_symmetric_trees(self, left_node: TreeNode, right_node: TreeNode) -> bool:
        if left_node is None and right_node is None:
            return True
        if left_node is not None and right_node is None:
            return False
        if left_node is None and right_node is not None:
            return False
        is_equal_roots = left_node.val == right_node.val
        is_equal_outers = self.is_symmetric_trees(left_node.left, right_node.right)
        is_equal_inners = self.is_symmetric_trees(left_node.right, right_node.left)
        return is_equal_roots and is_equal_outers and is_equal_inners
