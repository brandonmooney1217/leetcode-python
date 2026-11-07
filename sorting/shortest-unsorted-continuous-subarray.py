class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        tmp = sorted(nums)

        l = 0
        while l < len(nums) and tmp[l] == nums[l]:
            l+=1

        r = len(nums)-1

        while r >= 0 and nums[r] == tmp[r]:
            r-=1

        if l > r:
            return 0
        return r-l+1
