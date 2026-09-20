class Solution:
    def canJump(self, nums: list[int]) -> bool:
        frontier = nums[0]

        for i in range(1, len(nums)):
            if i > frontier:
                return False
            frontier = max(frontier, i + nums[i])

        return True
