import collections

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        res = 0
        l = 0
        pair_count = 0
        dct = collections.defaultdict(int)

        for r in range(len(nums)):
            num = nums[r]
            dct[num] +=1
            pair_count += dct[num]-1

            while pair_count >=k:
                res += len(nums)-r
                pair_count -= dct[nums[l]]-1
                dct[nums[l]] -=1
                l+=1
        return res
