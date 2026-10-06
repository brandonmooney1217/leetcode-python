class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            if i > 0 and  nums[i] == nums[i-1]:
                continue
            target = nums[i] * -1
            l, r = i+1, len(nums)-1

            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    l +=1
        return list(res)
