
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        def f(node):
            if not node:
                return 0

            left = f(node.left)
            right = f(node.right)

            tmp = max(left, right) + 1
            tmp2 = left+right
            self.res = max(self.res, left+right)

            return max(left, right) + 1

        f(root)
        return self.res
