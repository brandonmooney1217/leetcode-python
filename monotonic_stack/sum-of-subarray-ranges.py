class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        """
        mn - 1
        [1] [1,2] [1,2,3]
        sm = 3

        mn - 2
        [2] [2,3]
        sm = 4

        mn-3
        [3]
        sm = 3

        COMBINED SUM = 10

        -----
        mx-1
        [1]
        sm = 1

        mx-2
        [1,2], [2]
        sm = 4

        mx-3
        [1,2,3] [2,3] [3]
        sm = 9

        COMBINED SUM 14

        """

        n = len(nums)
        mn_left = [1] * n
        mn_right = [1] * n
        MOD = 10**9 + 7

        stack = []
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            mn_left[i] = i+1 if not stack else i - stack[-1]
            stack.append(i)

        # reset stack
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]:
                stack.pop()
            mn_right[i] = n-i if not stack else stack[-1] - i
            stack.append(i)
        mn_sum = 0
        for num, l, r in zip(nums, mn_left, mn_right):
            mn_sum = (mn_sum + (num*l*r))
        print(mn_sum)
        print(nums)
        print(mn_left)
        print(mn_right)


        mx_left = [1] * n
        mx_right = [1] * n
        MOD = 10**9 + 7

        stack = []
        for i in range(n):
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            mx_left[i] = i+1 if not stack else i - stack[-1]
            stack.append(i)

        # reset stack
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                stack.pop()
            mx_right[i] = n-i if not stack else stack[-1] - i
            stack.append(i)

        mx_sum = 0
        for num, l, r in zip(nums, mx_left, mx_right):
            mx_sum = (mx_sum + (num*l*r))
        return mx_sum - mn_sum
