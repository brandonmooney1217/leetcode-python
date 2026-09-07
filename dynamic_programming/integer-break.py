class Solution:
    def integerBreak(self, n: int) -> int:
        if n <=3:
            return n-1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for num in range(4, n+1):
            res = 0
            for i in range(num+1):
                res = max(res, dp[i] * dp[num-i])
            dp[num] = res
        return dp[n]
