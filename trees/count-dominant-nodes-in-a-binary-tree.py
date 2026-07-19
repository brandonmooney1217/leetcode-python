# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            if not node.left and not node.right:
                return [1, node.val] # return count, max in that subtree

            left = dfs(node.left)
            right = dfs(node.right)
            mx = max(left[1], right[1])

            count = 0
            count = count + left[0] + right[0]
            if node.val >= left[1] and node.val >= right[1]:
                count +=1
                mx = node.val

            return [count, mx]
        return dfs(root)[0]
