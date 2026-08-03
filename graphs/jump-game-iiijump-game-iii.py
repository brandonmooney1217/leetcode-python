from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)
        seen = set()
        def dfs(index):
            if arr[index] == 0:
                return True
            if index in seen:
                return False

            seen.add(index)
            left = False
            right = False

            if (index-arr[index]) >= 0:
                left = dfs(index-arr[index])
            if (index+arr[index]) < n:
                right = dfs(index+arr[index])

            return left or right
        return dfs(start)
