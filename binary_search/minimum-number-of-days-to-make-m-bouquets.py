
from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if n < m*k:
            return -1

        def can(test_day):
            count = 0
            streak = 0

            for d in bloomDay:
                if d > test_day:
                    streak = 0
                    continue

                streak +=1
                if streak == k:
                    count +=1
                    streak = 0

            return count >= m
        l, r = min(bloomDay), max(bloomDay)
        res = 0
        while l <= r:
            mid = (l+r) //2
            tmp = can(mid)
            if tmp:
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
