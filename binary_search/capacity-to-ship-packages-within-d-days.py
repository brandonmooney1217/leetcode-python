
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def getDays(test_weight):
            count = 0
            curr = 0
            for w in weights:
                if (curr+w) > test_weight:
                    count +=1
                    curr = w
                else:
                    curr +=w
            if curr > 0:
                count +=1
            return count <= days

        sm = sum(weights)
        l, r = max(weights), sm
        res = 0
        while l <= r:
            mid = (l+r) //2
            test = getDays(mid)
            print(mid, test)
            if test:
                r = mid-1
                res = mid
            else:
                l = mid+1
        return res
