
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        [0, 2, 5, 6, 8, 12, 15]

        """
        n = len(nums)
        prefix = [0] * (n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        print(prefix)
        res = float('inf')

        for i in range(n):
            need = target + prefix[i]
            l = i+1
            r = n+1

            while l < r:
                mid = (l+r)//2
                if prefix[mid]< need:
                    l = mid+1
                else:
                    r = mid
            if l <= n:
                res = min(res, l-i)

        return res if res!=float('inf') else 0
