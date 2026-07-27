from typing import List
import collections


"""
Do edges have weights?
    /        \
    NO          YES
    /            \
Use BFS       Are any weights negative?
                /          \
                NO            YES
            /                \
        Use Dijkstra       Use Bellman-Ford /
                            SPFA
"""
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        seen = {}
        seen[(0, 0)] = k

        queue = collections.deque()
        queue.append((0, 0, k, 0)) # r, c, removals, steps

        while queue:
            row, col, removals, steps = queue.popleft()
            if row == rows-1 and col == cols-1:
                return steps

            for dr, dc in directions:
                xr, xc = dr+row, dc+col

                if xr in range(rows) and xc in range(cols):
                    x_removals = removals - grid[xr][xc]
                    x_steps = steps+1

                    if x_removals >= 0 and x_removals > seen.get((xr, xc), -1):
                        seen[(xr,xc)] = x_removals
                        queue.append((xr, xc, x_removals, x_steps))
        return -1
