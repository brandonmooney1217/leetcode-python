from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        dp = [1] * n # length of longest inc subsequence end at i
        dp_count = [1] * n # count of number longest in sub end at i
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        dp_count[i] = dp_count[j]
                    elif dp[j] + 1 == dp[i]:
                        dp_count[i] += dp_count[j]
                res = max(res, dp[i])

        count = 0
        for mx, freq in zip(dp, dp_count):
            if mx == res:
                count += freq

        return count
