class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        sm = sum(nums)
        if sm % k != 0:
            return False
        target = sm //k

        nums.sort(key = lambda x: -x)
        res = [0] * k

        """
        we know k * target == total sum
        the only way where the sum of each of the k buckets is <= target is if they equal target
        """
        def dfs(index):
            if index == len(nums):
                return True

            for i in range(k):
                if i > 0 and res[i] == res[i-1]:
                    continue

                if nums[index] + res[i] <= target:
                    res[i] += nums[index]
                    if dfs(index+1):
                        return True
                    res[i] -=nums[index]
                    if res[i] == 0:
                        return False
            return False
        return dfs(0)
