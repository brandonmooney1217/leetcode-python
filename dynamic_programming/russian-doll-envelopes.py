# LeetCode #354 (Hard): https://leetcode.com/problems/russian-doll-envelopes/
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key = lambda x: (x[0], x[1] * -1))

        res = 1
        stack = []

        for i in range(n):
            if not stack or envelopes[i][1] > stack[-1]:
                stack.append(envelopes[i][1])
            else:
                l, r = 0, len(stack)-1
                while l < r:
                    mid = (l+r) //2
                    if envelopes[i][1] > stack[mid]:
                        l = mid+1
                    else:
                        r = mid
                stack[l] = envelopes[i][1]


            res = max(res, len(stack))
        return res
