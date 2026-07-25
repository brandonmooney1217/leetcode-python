# Status: needs-review
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def f(node):
            if not node:
                return (-1, -1) #left, right

            left = f(node.left)
            right = f(node.right)

            goLeft = 1 + left[1]
            goRight = 1 + right[0]

            self.res = max(self.res, goLeft, goRight)
            return (goLeft, goRight)
        f(root)
        return self.res
