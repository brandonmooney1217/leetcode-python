class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx_num = max(nums)
        res = 0
        count = 0
        left = 0

        for i in range(len(nums)):
            num = nums[i]
            if num == mx_num:
                count +=1

            while count == k:
                res += (len(nums)-i)
                if nums[left] == mx_num:
                    count -=1
                left +=1
        return res
