class Solution:
    def numDecodings(self, s: str) -> int:
        """
        2 2 6
        1 2 2
        algorithm
            - move from left to right
            - if number is 3-9, then just copy whatever is to left of it and append number
            - if number is to left 1, then add whatever is to left by 2
            - if number is to left is 2, check if if curr num is 0 - 6
            - if number is 0, then skip
        """
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(1, n):
            curr_num = s[i]
            prev_num = s[i-1]

            # append to existing, so copy
            if curr_num != "0":
                dp[i+1] = dp[i]

            # check if we can concatenate
            if prev_num == "1":
                dp[i+1] += dp[i-1]

            if prev_num == "2":
                if curr_num in "0123456":
                    dp[i+1] += dp[i-1]
        return dp[n]
