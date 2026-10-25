class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        """

        nums = [1,1,1,2,3], target = 4, total sm = 8

        target % sum(nums) = 4


        """
        n = len(nums)
        sm = sum(nums)

        remainder = target % sm
        cycles = target //sm

        if remainder == 0:
            return cycles * n

        arr = nums + nums
        curr_sm = 0
        l = 0
        res = float('inf')
        for r in range(len(arr)):
            curr_sm += arr[r]
            while l <=r and (curr_sm > remainder or (r-l+1) > n):
                curr_sm -= arr[l]
                l+=1

            if curr_sm == remainder:
                res = min(res, r-l+1)
        if res == float('inf'):
            return -1

        return res + (n*cycles)
