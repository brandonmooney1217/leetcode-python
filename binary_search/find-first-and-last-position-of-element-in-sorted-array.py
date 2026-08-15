class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r, = 0, n

        res = [-1, -1]

        while l < r:
            mid = (l+r) //2
            if nums[mid] == target:
                res[0] = mid
                r = mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid

        l, r, = 0, n
        while l < r:
            mid = (l+r) //2
            if nums[mid] == target:
                res[1] = mid
                l = mid +1
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid

        return res
