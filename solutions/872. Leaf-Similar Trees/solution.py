from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        first, second = [], []
        self.get_leafs(root1, first)
        self.get_leafs(root2, second)
        if len(first) != len(second):
            return False
        for el1, el2 in zip(first, second):
            if el1 != el2:
                return False
        return True

    def get_leafs(self, node: TreeNode, nodes_list: List[int]):
        if node is None:
            return
        if node.left is None and node.right is None:
            nodes_list.append(node.val)
            return
        if node.left is None:
            self.get_leafs(node.right, nodes_list)
            return
        if node.right is None:
            self.get_leafs(node.left, nodes_list)
            return
        self.get_leafs(node.left, nodes_list)
        self.get_leafs(node.right, nodes_list)
