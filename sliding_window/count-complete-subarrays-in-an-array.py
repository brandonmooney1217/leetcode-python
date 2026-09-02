class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        seen = set(nums)
        target = len(seen)
        res = 0
        left = 0
        dct = collections.defaultdict(int)

        for index, val in enumerate(nums):
            dct[val] +=1

            while len(dct) == target:
                res += (len(nums)-index)
                dct[nums[left]] -=1
                if dct[nums[left]] == 0:
                    del dct[nums[left]]
                left +=1
        return res
