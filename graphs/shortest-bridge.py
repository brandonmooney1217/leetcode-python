from typing import List
import collections

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        seen = set()
        queue = collections.deque()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r,c) in seen or grid[r][c] != 1:
                return

            seen.add((r,c))
            queue.append((r,c, 0))
            grid[r][c] = 2
            for dr, dc in directions:
                xr, xc = dr+r, dc+c
                dfs(xr, xc)

        found=False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    found=True
                    dfs(i, j)
                    break
            if found:
                break

        while queue:
            r, c, count = queue.popleft()
            if grid[r][c] == 1:
                return count-1

            for dr, dc in directions:
                xr, xc = dr+r, dc+c
                if xr in range(rows) and xc in range(cols) and (xr,xc) not in seen:
                    seen.add((xr, xc))
                    queue.append((xr, xc, count+1))

        return -1
