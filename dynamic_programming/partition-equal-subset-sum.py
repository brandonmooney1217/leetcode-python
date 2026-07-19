from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        amount = sm //2
        if sm % 2 == 1:
            return False

        n = len(nums)
        dp = [[False for _ in range(amount+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):

            num = nums[i-1]
            for sm in range(1, amount+1):
                # dont use value
                dp[i][sm] = dp[i-1][sm] or dp[i][sm]

                # use this value
                if sm >= num:
                    dp[i][sm] = dp[i][sm] or dp[i-1][sm-num]
        return dp[n][amount]
