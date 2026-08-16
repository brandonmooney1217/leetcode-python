from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            mid = (l+r) // 2

            left_num = nums[mid-1] if (mid-1) > -1 else float('-inf')
            right_num = nums[mid+1] if (mid+1) < n else float('-inf')
            mid_num = nums[mid]

            if mid_num > left_num and mid_num > right_num:
                return mid
            elif left_num > mid_num:
                r = mid-1
            else:
                l = mid+1
        return l
