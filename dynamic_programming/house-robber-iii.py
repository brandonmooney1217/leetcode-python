
from typing import Optional
from functools import cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        """
        need to find max rob
        cannot rob 2 adjacent nodes
        organized into binary tree
            node - has child nodes
        """
        @cache
        def f(node, canRob):
            if not node:
                return 0

            skip, take = 0, 0

            if canRob:
                take = f(node.left, False) + f(node.right, False) + node.val

            skip = f(node.left, True) + f(node.right, True)

            return max(skip, take)
        return f(root, True)
