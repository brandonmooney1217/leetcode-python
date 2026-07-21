class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        """
        [0, 1, 2, 3],
        [1, 0, 0, 0],
        [2, 0, 0, 0],
        [3, 0, 0, 0],
        [4, 0, 0, 0],
        [5, 0, 0, 0]

        @cache
        def dfs(i, j):
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            else:
                replace = dfs(i+1, j+1) + 1
                insert = dfs(i, j+1) +1
                delete = dfs(i+1, j) +1

                return min(replace, insert, delete)
        return dfs(0, 0)
        """
        n, m = len(word1), len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            c1 = word1[i-1]
            for j in range(1, m+1):
                c2 = word2[j-1]

                if c1 == c2:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[n][m]
