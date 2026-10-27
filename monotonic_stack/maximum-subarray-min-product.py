class Solution:
    def maxSumMinProduct(self, nums: list[int]) -> int:
        left = [0] * len(nums)
        stack = []
        MOD = 10 ** 9 + 7

        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                stack.pop()
            left[i] = i+1 if not stack else i-stack[-1]
            stack.append(i)
        right = [0] * len(nums)
        stack = []

        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            right[i] = stack[-1]-i if stack else len(nums)-i
            stack.append(i)
        prefix = [0]
        for num in nums:
            prefix.append((prefix[-1] + num))



        res = 0
        for i in range(len(nums)):
            mn = nums[i]
            left_side = i-left[i] + 1
            right_side = i + right[i]
            sm = prefix[right_side]-prefix[left_side]
            res = max(res, sm * mn)

        return res % MOD

        """

        sm = nums[i] *
        left = index-left[i] + 1
        right = index + right[i]

        """
