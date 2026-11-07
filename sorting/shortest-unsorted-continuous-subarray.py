class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        r = -1
        mx = float('-inf')

        for i in range(n):
            curr = nums[i]
            if curr < mx:
                r = i
            mx = max(mx, curr)

        mn = float('inf')
        l = -1

        for i in range(n-1, -1, -1):
            curr = nums[i]
            if curr > mn:
                l = i
            mn = min(mn, curr)

        if l == -1 and r == -1:
            return 0
        return r-l+1
