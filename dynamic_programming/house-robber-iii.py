
from typing import Optional
from functools import cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        dp[i][parentRobbed] = state is current node and if parent was robbed

        if parentRobbed, then cannot rob

        if NOT parentRobbed
            - we can rob
            - can skip
            return mx of two above
        """
        @cache
        def f(node, p_robbed):
            if not node:
                return 0

            if p_robbed == 0:
                rob = f(node.left, 1) + f(node.right, 1) + node.val
                skip = f(node.left, 0) + f(node.right, 0)
                return max(rob, skip)

            else:
                return f(node.left, 0) + f(node.right, 0)
        return f(root, 0)
