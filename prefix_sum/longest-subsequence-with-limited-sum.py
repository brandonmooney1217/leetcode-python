
from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        prefix = [0] * (n+1)
        res = []
        nums.sort()

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        for val in queries:
            l, r = 0, n+1
            while l < r:
                mid = (l+r)//2

                if prefix[mid] <= val:
                    l = mid+1
                else:
                    r = mid

            res.append(l-1)
        return res
