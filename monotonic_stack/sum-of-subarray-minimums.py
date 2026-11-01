class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)

        left = [0] * n
        stack = []

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            left[i] = i-stack[-1] if stack else i+1
            stack.append(i)
        right = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n-i
            stack.append(i)

        MOD = 10**9 + 7
        res = 0
        for l, r, n, in zip(left, right, arr):
            res = (res + (l*r*n))%MOD
        return res
