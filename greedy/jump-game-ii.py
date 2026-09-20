class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0
        res = 1
        furthest = nums[0]
        frontier = nums[0]

        for i in range(1, len(nums)):
            val = nums[i]
            if i > frontier:
                res +=1
                frontier = furthest
            furthest = max(furthest, i + val)
        return res
