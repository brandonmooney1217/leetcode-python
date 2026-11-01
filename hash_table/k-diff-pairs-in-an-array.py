# LeetCode #532 (Medium): https://leetcode.com/problems/k-diff-pairs-in-an-array/
from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dct = Counter(nums)
        if k == 0:
            return sum(1 for num in dct.values() if num > 1)
        count = 0
        for num in dct.keys():
            if (k+num) in dct:
                count +=1

        return count
