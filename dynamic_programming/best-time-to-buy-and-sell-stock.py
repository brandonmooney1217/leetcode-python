from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = float('inf')

        for num in prices:
            if num < buy:
                buy = num
                continue

            res = max(res, num-buy)


        return res
