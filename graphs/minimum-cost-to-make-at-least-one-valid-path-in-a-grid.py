from typing import List
import heapq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        def getCost(i, j, sign):
            if sign == 1:
                return 0 if i == 0 and j == 1 else 1
            elif sign == 2:
                return 0 if i == 0 and j == -1 else 1
            elif sign == 3:
                return 0 if i == 1 and j == 0 else 1
            else:
                return 0 if i == -1 and j == 0 else 1

        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        seen = {}
        seen[(0, 0)] = 0

        minHeap = [(0, 0, 0)] # cost, row, col

        while minHeap:
            cost, row, col = heapq.heappop(minHeap)
            sign = grid[row][col]

            if row == rows-1 and col == cols-1:
                return cost

            if cost > seen.get((row, col), float('inf')):
                continue

            for dr, dc in directions:
                xr, xc = dr + row, dc + col
                if xr in range(rows) and xc in range(cols):
                    new_cost = cost + getCost(dr, dc, sign)

                    if new_cost < seen.get((xr, xc), float('inf')):
                        seen[(xr, xc)] = new_cost
                        heapq.heappush(minHeap, (new_cost, xr, xc))

        return -1
