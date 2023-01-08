from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return None
        queue = [(root, 0)]
        prev_node, prev_level = None, -1
        while queue:
            node, level = queue[0]
            queue.pop(0)
            node.next = prev_node if prev_level == level else None
            prev_node, prev_level = node, level
            if node.right is None and node.left is None:
                continue
            queue.append((node.right, level + 1))
            queue.append((node.left, level + 1))
        return root
