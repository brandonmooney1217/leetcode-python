class Solution:
    def minInsertions(self, s: str) -> int:

        """
        @cache
        def f(l, r):
            if l >= r:
                return 0

            if s[l] == s[r]:
                return f(l+1, r-1)
            else:
                add_left = f(l+1, r) + 1
                add_right = f(l, r-1) + 1
                return min(add_left, add_right)
        return f(0, len(s)-1)
        """

        n = len(s)

        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for i in range(n-1):
            if s[i] != s[i+1]:
                dp[i][i+1] = 1


        for length in range(3, n+1):
            for start in range(n-length+1):
                end = start + length - 1
                if s[start] == s[end]:
                    dp[start][end] = dp[start+1][end-1]
                else:
                    dp[start][end] = min(dp[start+1][end], dp[start][end-1]) + 1
        print(dp)
        return dp[0][-1]
