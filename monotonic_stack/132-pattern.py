class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        second = float('-inf')
        n = len(nums)
        stack = []

        for i in range(n-1, -1, -1):
            if nums[i] < second:
                return True

            while stack and nums[i] > stack[-1]:
                second = stack.pop()
            stack.append(nums[i])
        return False
