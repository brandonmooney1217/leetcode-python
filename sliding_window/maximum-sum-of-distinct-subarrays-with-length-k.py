# LeetCode #2461 (Medium): https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
import collections

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        seen = collections.defaultdict(int)
        res = 0
        l = 0
        sm = 0

        for i in range(len(nums)):
            sm += nums[i]
            seen[nums[i]] +=1

            if i >= (k-1):
                if len(seen) == k:
                    res = max(res, sm)
                if nums[l] in seen:
                    seen[nums[l]] -=1
                    if seen[nums[l]] == 0:
                        del seen[nums[l]]
                sm -= nums[l]
                l+=1

        return res
