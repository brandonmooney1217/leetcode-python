# LeetCode #740 (Medium): https://leetcode.com/problems/delete-and-earn/
import collections

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        dct = collections.defaultdict(int)
        for num in nums:
            dct[num] += num

        arr = list(set(nums))
        arr.sort()
        p2 = -1
        p1 = arr[0]
        sm1 = dct[arr[0]]
        sm2 = 0
        res = dct[arr[0]]

        for i in range(1, len(arr)):
            tmp = p1
            tmp_sm = sm1
            if arr[i] > p1+1:
                sm1 += dct[arr[i]]
                sm2 = tmp_sm
                p1 = arr[i]
                p2 = tmp
            else:
                if sm2+dct[arr[i]] > sm1:
                    sm1 = sm2 + dct[arr[i]]
                    sm2 = tmp_sm
                    p1 = arr[i]
                    p2 = tmp
                else:
                    sm2 = tmp_sm
                    p2 = tmp
            res = max(res, sm1, sm2)

        return res
