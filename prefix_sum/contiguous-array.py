# LeetCode #525 (Medium): https://leetcode.com/problems/contiguous-array/
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        seen = {}
        seen[0] = -1
        sm = 0

        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                sm -=1
            else:
                sm +=1

            if sm not in seen:
                seen[sm] = i
            else:
                res = max(res, i-seen[sm])

        return res
