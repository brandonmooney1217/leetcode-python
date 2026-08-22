class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        mx = max(m, n)

        for i in range(m):
            for j in range(n):
                up = dp[i-1][j] if (i-1) >= 0 else 0
                left = dp[i][j-1] if (j-1) >= 0 else 0
                diagonal = dp[i-1][j-1] if ((i-1) >= 0 and (j-1) >= 0) else 0

                dp[i][j] += up + left + mat[i][j] - diagonal
        res = 0
        for i in range(m):
            for j in range(n):
                if i >= res and j >= res:
                    k = res + 1
                    row = i-k
                    col = j-k

                    top = dp[row][j] if row >= 0 else 0
                    left = dp[i][col] if col >= 0 else 0
                    diag = dp[row][col] if (row >= 0 and col >= 0) else 0

                    sm = dp[i][j] + diag - top - left
                    if sm <= threshold:
                        res +=1
        return res


    """
    [
    [1,1,3,2,4,3,2],
    [1,1,3,2,4,3,2],
    [1,1,3,2,4,3,2]
    ]

    [
    [1, 2, 5,   7, 11, 14, 16],
    [2, 4, 10, 14, 22, 28, 32],
    [3, 6, 15, 21, 33, 42, 48]
    ]
    """
