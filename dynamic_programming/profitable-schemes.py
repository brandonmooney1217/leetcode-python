from functools import cache

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        MOD = 10**9 + 7
        """
        length = 100
        profit = 100
        group count = 100
        """
        @cache
        def dfs(index, group_count, profit_count):
            if index == len(group):
                return profit_count == minProfit

            take = 0
            if (group_count + group[index]) <= n:
                take = dfs(index+1, group_count + group[index], min(minProfit, profit[index] + profit_count))
            skip = dfs(index+1, group_count, profit_count)

            return (skip + take) % MOD
        return dfs(0, 0, 0)
