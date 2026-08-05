from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        [0,0,0,0]
        [0,0,1,0]
        [0,1,1,0]
        [0,0,0,0]


        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
        """

        rows, cols = len(grid),len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        count = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols):
                return
            if grid[r][c] == 0:
                return

            grid[r][c] = 0

            for dr, dc in directions:
                xr, xc = dr+r, dc + c
                dfs(xr, xc)
        for i in range(rows):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][cols-1] == 1:
                dfs(i, cols-1)

        for j in range(cols):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[rows-1][j] == 1:
                dfs(rows-1, j)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:count+=1

        return count
