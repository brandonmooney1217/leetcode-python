# LeetCode #283 (Easy): https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1 3 3 0 3
            l.  r
        """

        l, r = 0, 0
        while r < len(nums):
            if nums[r] == 0:
                r+=1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r+=1
