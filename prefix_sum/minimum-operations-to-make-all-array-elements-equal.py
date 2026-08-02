from typing import List

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:

        """
        1. sort the nums array so you can split array into nums greater than q and less than q
        2. calculate prefix sums - needed for maht later
        3. iterate through each query
            3a. find index that divides greater than nums and less than nums
            3b. left_count = (number of nums less than q) * q - sum until that point
            3c. right_count = right sum - (number of nums greater than q) * q
            3d. append to res
        """
        n = len(nums)
        nums.sort()

        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        res = []

        def lower_bound(target):
            l, r = 0, n

            while l < r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid
            return l

        for query in queries:
            idx = lower_bound(query)

            left_sum = prefix[idx]
            left_count = idx
            left_cost = (query * left_count) - left_sum

            right_sum = prefix[n] - prefix[idx]
            right_count = n -idx
            right_cost = right_sum - (query * right_count)

            res.append(left_cost + right_cost)

        return res
