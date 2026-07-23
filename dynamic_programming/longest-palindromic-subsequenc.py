
from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def f(l, r):
            if l == r:
                return 1
            if l > r:
                return 0

            if s[l] == s[r]:
                return f(l+1, r-1) + 2
            else:
                return max(f(l+1, r), f(l, r-1))
        return f(0, len(s)-1)
