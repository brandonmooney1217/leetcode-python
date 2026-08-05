
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [-1,0], [0, -1]]
        res = 0
        seen = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols):
                return 0
            if (r,c) in seen:
                return 0

            if grid[r][c] == 0:
                return 0

            count = 1
            seen.add((r,c))
            for dr, dc in directions:
                xr, xc = dr+r, dc+c
                count += dfs(xr, xc)
            return count

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and grid[r][c] == 1:
                    res = max(dfs(r,c), res)


        return res
