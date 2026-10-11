class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n):
            for word in wordDict:
                if len(word) > (i+1):
                    continue

                if word == s[i-len(word)+1:i+1]:
                    dp[i+1] = dp[i-len(word) + 1] or dp[i+1]
        return dp[n]
