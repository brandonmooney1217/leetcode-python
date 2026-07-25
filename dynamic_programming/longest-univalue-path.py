# Status: needs-review
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        def f(node):
            if not node:
                return 0

            left = f(node.left)
            right = f(node.right)

            left_chain, right_chain = 0, 0

            if node.left and node.left.val == node.val:
                left_chain = left + 1
            if node.right and node.right.val == node.val:
                right_chain = right + 1

            self.res = max(self.res, left_chain + right_chain)
            return max(left_chain, right_chain)
        f(root)
        return self.res
