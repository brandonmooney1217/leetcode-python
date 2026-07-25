# Status: needs-review
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def f(node):
            if not node:
                return 0

            left = f(node.left)
            right = f(node.right)

            # need to return coin surplus at each state
            self.moves += abs(left) + abs(right)
            return node.val + left + right - 1
        f(root)
        return self.moves
