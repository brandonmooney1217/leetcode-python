from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for num in range(1, amount+1):
            for coin in coins:
                if num >= coin:
                    dp[num] = min(dp[num], dp[num-coin] + 1)

        tmp = dp[amount]

        return tmp if tmp != amount + 1 else -1
