from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        """
        n = len(nums)
        dp = [1] * n

        for i in range(n-1, -1, -1):
            curr_num = nums[i]
            for j in range(i+1, n):
                if curr_num < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        """
        res = 0
        stack = []

        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
            else:
                l, r = 0, len(stack)
                while l < r:
                    mid = (l+r)//2

                    if stack[mid] < num:
                        l = mid + 1
                    else:
                        r = mid
                stack[l] = num

            res = max(res, len(stack))

        return res
