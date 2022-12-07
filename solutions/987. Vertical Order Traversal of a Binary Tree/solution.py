import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_min, col_max = float('inf'), -float('inf')
        ans = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            tmp = collections.defaultdict(list)
            for _ in range(len(queue)):
                node, col = queue.pop(0)
                tmp[col].append(node.val)
                if node.left is not None:
                    queue.append((node.left, col - 1))
                    col_max = max(col_max, col)
                    col_min = min(col_min, col - 1)
                if node.right is not None:
                    queue.append((node.right, col + 1))
                    col_max = max(col_max, col + 1)
                    col_min = min(col_min, col)
            for key in tmp:
                ans[key].extend(sorted(tmp[key]))
        return [
            ans[i]
            for i in range(col_min, col_max + 1)
        ]
