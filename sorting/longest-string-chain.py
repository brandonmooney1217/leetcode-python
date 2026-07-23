from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def helper(w1, w2):
            i, j = 0, 0
            count = 0
            while i < len(w1) and j < len(w2):
                if w1[i] != w2[j]:
                    count +=1
                    j+=1

                    if count > 1:
                        break
                else:
                    i +=1
                    j +=1
            return count <= 1

        dp = {}
        for word in words:
            dp[word] = 1
        res = 1
        words.sort(key = lambda x: len(x))

        for word in words:
            for key, val in dp.items():
                if len(word) != len(key) + 1:
                    continue

                tmp = helper(key, word)
                if tmp:
                    dp[word] = max(dp[word], val + 1)
                    res = max(res, dp[word])
        return res
