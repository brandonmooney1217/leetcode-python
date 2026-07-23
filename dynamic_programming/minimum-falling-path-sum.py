from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])

        dp = [[float('inf') for _ in range(cols+2)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                dp[i][j+1] = matrix[i][j]

        for i in range(rows-2, -1, -1):
            for j in range(cols, -1, -1):
                dp[i][j] = min(dp[i+1][j+1], dp[i+1][j-1], dp[i+1][j]) + dp[i][j]
        return min(dp[0])
