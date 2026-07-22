from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        l, r = 1, max(piles)

        # binary search on answer - lower bound
        while l < r:
            mid = (l+r) //2
            hours_count = 0
            for p in piles:
                hr = math.ceil(p/mid)
                hours_count += hr

            if hours_count > h:
                l = mid+1
            else:
                r = mid
        return l
