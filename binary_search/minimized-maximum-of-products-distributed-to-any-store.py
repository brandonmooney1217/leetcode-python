from typing import List
import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        sm = sum(quantities)
        l, r = 1, sm

        def can(test):
            count = 0
            for q in quantities:
                count += math.ceil(q/test)

            return count <= n

        while l <= r:
            mid = (l+r)//2
            tmp = can(mid)

            if tmp:
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
