# LeetCode #1423 (Medium): https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        window = n-k
        sm = sum(cardPoints)
        res = float('inf')
        l = 0

        if k == n:
            return sm

        curr = 0
        for i in range(len(cardPoints)):
            curr +=cardPoints[i]

            if i >= window-1:
                res = min(res, curr)

                curr-= cardPoints[l]
                l+=1
        return sm-res
