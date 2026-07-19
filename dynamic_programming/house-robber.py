from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        t1, t2, = 0, 0
        for num in nums:
            tmp = t2
            # t1 + num => rob this house
            # keep t2 => skip this house
            t2 = max(t2, t1+num)
            t1 = tmp
        return t2
