class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        """
        [1,2,3],
        [4,5,6],
        [7,8,9]

        [0, 0,  0,   0],
        [0, 1,  3,   6],
        [0, 5,  12, 21],
        [0, 12, 27, 45]]

        [12,21,16],
        [27,45,33],
        [24,39,28]]

        1  3  6
        5  12 21
        12 27.45

        """
        rows, cols = len(mat), len(mat[0])
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]

        for i in range(rows):
            for j in range(cols):
                dp[i+1][j+1] = mat[i][j] + dp[i+1][j] + dp[i][j+1] - dp[i][j]
        print(dp)
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                r1, r2 = max(0, r-k), min(rows-1, r+k)
                c1, c2 = max(0, c-k), min(cols-1, c+k)

                whole = dp[r2+1][c2+1]
                top = dp[r1][c2+1]
                left = dp[r2+1][c1]
                corner = dp[r1][c1]

                res[r][c] = whole - top - left + corner


        return res
