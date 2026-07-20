from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """"
        @cache
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return dfs(i+1, j+1) + 1
            else:
                tmp1 = dfs(i, j+1)
                tmp2 = dfs(i+1, j)
                return max(tmp2, tmp1)
        return dfs(0, 0)
        """
        n, m = len(text1), len(text2)

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            c1 = text1[i]
            for j in range(m-1, -1, -1):
                c2 = text2[j]

                if c1 == c2:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
