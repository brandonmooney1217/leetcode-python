from typing import List
import collections

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dct = collections.defaultdict(int)
        l, res = 0, 0

        for r in range(len(nums)):
            dct[nums[r]] +=1

            while l < r and dct[nums[r]] > k:
                dct[nums[l]] -=1
                l+=1

            res = max(res, r-l+1)

        return res
