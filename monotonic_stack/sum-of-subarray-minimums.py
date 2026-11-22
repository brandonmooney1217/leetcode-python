class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        left = [1] * n
        right = [1] * n
        res = 0
        MOD = 10**9 + 7

        stack = []
        for i in range(n):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            left[i] = i+1 if not stack else i - stack[-1]
            stack.append(i)

        # reset stack
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            right[i] = n-i if not stack else stack[-1] - i
            stack.append(i)

        for n, l, r in zip(arr, left, right):
            res = (res + (n*l*r)) %MOD
        return res
