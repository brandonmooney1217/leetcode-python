# LeetCode #974 (Medium): https://leetcode.com/problems/subarray-sums-divisible-by-k/
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        dct = {}
        dct[0] = 1
        sm = 0

        for index, num in enumerate(nums):
            sm += num
            remainder = sm % k

            if remainder not in dct:
                dct[remainder] = 1
            else:
                res += dct[remainder]
                dct[remainder] +=1
        return res
