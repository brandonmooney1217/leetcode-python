
from typing import List
import collections
from collections import Counter

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        queue = collections.deque()
        queue.append((entrance[0], entrance[1], 0))
        seen = set()
        seen.add((entrance[0], entrance[1]))

        while queue:
            row, col, count = queue.popleft()
            if (row == 0 or row == rows-1) and count != 0:
                return count

            if (col == 0 or col == cols-1) and count != 0:
                return count


            for dr, dc in directions:
                xr, xc = dr+row, dc+col

                if xr in range(rows) and xc in range(cols):
                    if (xr, xc) not in seen and maze[xr][xc] == ".":
                        seen.add((xr, xc))
                        queue.append((xr, xc, count+1))
        return -1
