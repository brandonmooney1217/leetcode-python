class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """
        [2,7,15]
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
        0 2 2 2 4 4 6 7 9
        """
        mx = max(days)
        dp = [float('inf')] * (mx+1)
        dp[0] = 0
        seen = set(days)

        for i in range(1, mx+1):
            if i not in seen:
                dp[i] = dp[i-1]
                continue

            for j in range(len(costs)):
                if j == 0:
                    dp[i] = min(dp[i], dp[i-1] + costs[j])

                elif j == 1:
                    index = max(i-7, 0)
                    dp[i] = min(dp[i], dp[index] + costs[j])

                else:
                    index = max(i-30, 0)
                    dp[i] = min(dp[i], dp[index] + costs[j])
        return dp[mx]
