class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        """
        Recursive solution with memoization
        s1 = a
        s2 = b
        s3 = a

        @cache
        def f(i, j):
            if (i+j) == len(s3):
                return True

            s1_char = s1[i] if i < len(s1) else ""
            s2_char = s2[j] if j < len(s2) else ""


            t1, t2 = False, False
            if s1_char == s3[i+j]:
                t1 = f(i+1, j)
            if s2_char == s3[i+j]:
                t2 = f(i, j+1)

            return t1 or t2
        return f(0, 0)
        """

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True

        # need to initialize first row and first column
        # handles the base case where one string is empty
        for i in range(1, len(s1) +1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, len(s2) +1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1) + 1):
            s1_char = s1[i-1]
            for j in range(1, len(s2) + 1):
                s2_char = s2[j-1]

                if s1_char == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]

                if s2_char == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        return dp[len(s1)][len(s2)]
