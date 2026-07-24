
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = float('-inf')
        def f(node):
            if not node:
                return 0

            left = max(0, f(node.left))
            right = max(0, f(node.right))

            self.res = max(self.res, left + right + node.val)
            return max(left, right) + node.val

        f(root)
        return self.res
