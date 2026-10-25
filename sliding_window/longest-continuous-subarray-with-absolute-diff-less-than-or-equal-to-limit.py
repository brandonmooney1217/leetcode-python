class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        res = 0
        mn, mx = collections.deque(), collections.deque()
        l = 0
        def helper(arr):
            tmp = []
            for num in arr:
                tmp.append(nums[num])
            return tmp


        for i in range(len(nums)):
            while mn and nums[i] < nums[mn[-1]]:
                mn.pop()
            mn.append(i)

            while mx and nums[i] > nums[mx[-1]]:
                mx.pop()
            mx.append(i)

            while (nums[mx[0]] - nums[mn[0]]) > limit:
                l+=1
                if mx[0] < l:
                    mx.popleft()
                if mn[0] < l:
                    mn.popleft()
            tmp = i - l + 1

            res = max(res, tmp)
        return res

        """
        1 4 10 2.  l = 8
        """
