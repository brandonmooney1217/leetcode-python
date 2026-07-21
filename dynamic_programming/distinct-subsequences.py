class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        impl
        - recursive approach
        - base case 1 - reach end of string t, then return 1
        - base casse 2 - reach end of s, then return 0, no more options
        - dp state is (i,j)

         @cache
         def f(i, j):
             if j == len(t):
                 return 1
             if i == len(s):
                 return 0

             if s[i] == t[j]:
                 # we can either choose to use s[i] or skip it
                 use_char = f(i+1, j+1)
                 skip_char = f(i+1, j)

                 return use_char + skip_char

             else:
                 return f(i+1, j)
         return f(0, 0)

        [1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 2, 1, 0, 0],
        [0, 1, 1, 3, 3, 0, 0],
        [0, 1, 1, 3, 3, 3, 0],
        [0, 1, 1, 3, 3, 3, 3]]
        """
        if len(t) > len(s):
            return 0

        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        for i in range(len(s)):
            dp[i][0] = 1

        for i in range(1, len(s) + 1):
            s_char = s[i-1]
            for j in range(1, len(t) + 1):
                t_char = t[j-1]

                dp[i][j] += dp[i-1][j]

                if t_char == s_char:
                    dp[i][j] += dp[i-1][j-1]
        return dp[len(s)][len(t)]
