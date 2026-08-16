class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1


        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                return mid

            # check for rotation point
            if nums[mid] < nums[n-1]:
                if target > nums[mid] and target <= nums[n-1]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target < nums[mid] and target >= nums[0]:
                    r = mid-1
                else:
                    l = mid+1
        return -1




        return -1
