from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        impl
            - recursive approach
            - dp state is dp[i][canSell]

            - if canSell state
                - we can either sell
                - or we can hold

            - if NOT canSell (can only buy)
                - we can buy
                - or we can skip and try to buy in the future
        """
        @cache
        def f(index, canSell):
            if index == len(prices):
                return 0
            if canSell == 1:
                sell = f(index+1, 0) + prices[index]
                hold = f(index+1, 1)
                return max(hold, sell)

            # only buy here
            else:
                buy = f(index+1, 1) - prices[index]
                skip = f(index+1, 0)
                return max(skip, buy)
        return f(0, 0)
