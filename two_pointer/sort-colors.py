# LeetCode #75 (Medium): https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        i = 0

        while i <=r:
            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r-=1
            elif nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l+=1
                i+=1
            else:
                i+=1
