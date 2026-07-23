from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        """
        [1, 0, 0],
        [0, 0, 0]
        """

        rows, cols = len(matrix), len(matrix[0])
        res = 0
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                else: dp[i][j] = 0

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if dp[i][j] == 0: continue

                dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1

                res = max(res, dp[i][j])
        return res ** 2
