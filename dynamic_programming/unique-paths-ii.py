from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        rows, cols = len(grid), len(grid[0])

        if grid[rows-1][cols-1] != 0: return 0

        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        dp[rows-1][cols-1] = 1


        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if i == rows-1 and j == cols-1: continue
                if grid[i][j] == 1: continue

                dp[i][j] = dp[i+1][j] + dp[i][j+1]



        return dp[0][0]
