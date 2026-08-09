from typing import List
class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                dp[i][j] = 1
                up = dp[i-1][j] if (i-1)>=0 else 0
                left = dp[i][j-1] if (j-1)>=0 else 0
                diagonal = dp[i-1][j-1] if (i-1)>=0 and (j-1)>=0 else 0
                dp[i][j] += min(left, up, diagonal)

        def can(k):
            valid_col = [False] * n

            for c in range(n):
                for r in range(m):
                    if dp[r][c] >=k:
                        valid_col[c] = True
                        break
            seen = False
            for c in range(n):
                if (c-k)>=0 and valid_col[c-k]:
                    seen = True
                if seen and valid_col[c]:
                    return True

            valid_row = [False] * m
            for r in range(m):
                for c in range(n):
                    if dp[r][c] >=k:
                        valid_row[r] = True
                        break

            seen = False
            for r in range(m):
                if (r-k)>=0 and valid_row[r-k]:
                    seen = True
                if seen and valid_row[r]:
                    return True
            return False



        left, right = 1, min(m, n)
        while left <= right:
            mid = (left+right)//2
            check = can(mid)
            if check:
                res = mid
                left = mid+1
            else:
                right = mid-1
        return res**2
