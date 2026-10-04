# LeetCode #11 (Medium): https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        1 8 1
        """
        l, r = 0, len(height)-1
        res = 0
        while l < r:
            left, right = height[l], height[r]
            area = min(left, right) * (r-l)
            res = max(res, area)

            if left > right:
                r-=1
            else:
                l+=1
        return res
