from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [-1,0], [0, -1]]
        count = 0

        def dfs(i, j):
            if not (i >= 0 and i < rows and j >=0 and j < cols) or (i,j) in seen:
                return
            if grid[i][j] == "0":
                return

            seen.add((i,j))
            for dr, dc in directions:
                xr, xc = i + dr, j + dc
                dfs(xr, xc)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in seen:
                    dfs(i, j)
                    count +=1

        return count
