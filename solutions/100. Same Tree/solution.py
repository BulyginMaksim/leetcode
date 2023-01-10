from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None or p is not None and q is None:
            return False
        left, right = [p], [q]
        while left and right:
            node1, node2 = left.pop(), right.pop()
            if node1.val != node2.val:
                return False
            if node1.left is not None and node2.left is not None:
                left.append(node1.left)
                right.append(node2.left)
            elif not (node1.left is None and node2.left is None):
                return False
            if node1.right is not None and node2.right is not None:
                left.append(node1.right)
                right.append(node2.right)
            elif not (node1.right is None and node2.right is None):
                return False

        return True
