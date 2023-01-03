from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node):
            if node is None:
                return
            for child_node in node.children:
                dfs(child_node)
            ans.append(node.val)
        dfs(root)
        return ans
