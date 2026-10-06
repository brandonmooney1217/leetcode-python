# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:

        curr = []
        res = []

        def f(node, sm):
            if not node:
                return
            curr.append(node.val)
            if node.val == sm and not node.left and not node.right:
                res.append(curr[:])

            if node.left:
                f(node.left, sm-node.val)
            if node.right:
                f(node.right, sm-node.val)
            curr.pop()

        f(root, targetSum)
        return res
