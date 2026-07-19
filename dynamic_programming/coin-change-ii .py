from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            coin = coins[i-1]
            for sm in range(1, amount+1):
                # copy whatever amount possible from prev coins used
                dp[i][sm] = dp[i-1][sm]

                if sm >=coin:
                    # correctly allows unlimited copies.
                    dp[i][sm] += dp[i][sm-coin]
        return dp[n][amount]
