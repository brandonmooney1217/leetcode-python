# LeetCode #18 (Medium): https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        if n < 4:
            return []
        print(nums)
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                goal = target - (nums[i] + nums[j])
                left, right = j+1, n-1
                while left < right:
                    if nums[left] + nums[right] == goal:
                        res.add(tuple([nums[i], nums[j], nums[left], nums[right]]))
                        left +=1
                        right -=1
                    elif nums[left] + nums[right] > goal:
                        right -=1
                    else:
                        left +=1
        return list(res)
