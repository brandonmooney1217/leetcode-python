class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        sm = 0
        res = 0
        left = 0

        for i in range(len(nums)):
            curr = nums[i]
            while curr in seen:
                sm -= nums[left]
                seen.remove(nums[left])
                left +=1
            seen.add(curr)
            sm += curr
            res = max(res, sm)

        return res
