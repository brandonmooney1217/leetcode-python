from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        canBuy -> 0
            we can either buy
            or we can skip
        canSell -> 1
            we can sell
            or we can hold
        cooldown-> 2
            need to wait
            transitions to 0

        """
        @cache
        def f(index, state):
            if index >= len(prices):
                return 0
            if state == 0:
                buy = f(index+1, 1) - prices[index]
                skip = f(index+1, 0)
                return max(buy, skip)
            elif state == 1:
                sell = f(index+1, 2) + prices[index]
                hold = f(index+1, 1)
                return max(sell, hold)
            else:
                return f(index+1, 0)
        return f(0,0)
