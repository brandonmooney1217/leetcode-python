
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can(target):
            curr_sm = 0
            count = 1

            for num in nums:
                if curr_sm + num > target:
                    count += 1
                    curr_sm = num
                else:
                    curr_sm += num

            return count <= k
        sm = sum(nums)
        res = 0
        left, right = max(nums), sm
        while left <= right:
            mid = (left+right)//2
            check = can(mid)
            if check:
                res = mid
                right = mid-1
            else:
                left = mid + 1
        return res
