import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        stack = collections.deque()
        res = []

        for i in range(len(nums)):
            curr = nums[i]

            # clear stack
            while stack and stack[0] < (i-k+1):
                stack.popleft()

            while stack and curr >= nums[stack[-1]]:
                stack.pop()
            stack.append(i)

            if i >= (k-1):
                res.append(nums[stack[0]])

        return res
