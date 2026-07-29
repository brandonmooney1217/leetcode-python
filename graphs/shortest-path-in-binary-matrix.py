from typing import List
import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        rows, cols = len(grid), len(grid[0])
        directions = [
            [0,1], [0,-1], [1,0], [-1,0],
            [1,1], [1,-1], [-1,-1], [-1,1]
        ]

        queue = collections.deque()
        queue.append((0, 0, 1)) # row, col, count
        seen = set()
        seen.add((0, 0))

        while queue:
            row, col, count = queue.popleft()
            if row == rows-1 and col == cols-1:
                return count

            for dr, dc in directions:
                xr, xc = row + dr, col + dc
                if xr in range(rows) and xc in range(cols):
                    if grid[xr][xc] == 0 and (xr, xc) not in seen:
                        seen.add((xr, xc))
                        queue.append((xr, xc, count+1))


        return -1
