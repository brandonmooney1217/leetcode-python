class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis, lds = [1] * n, [1] * n

        for i in range(n):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    lis[j] = max(lis[j], lis[i] + 1)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)
        res = 0
        for i in range(1, n-1):
            if lis[i] >1 and lds[i] >1:
                res = max(res, lis[i] + lds[i]-1)

        return n-res
