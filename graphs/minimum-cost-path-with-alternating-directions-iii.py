
from typing import List
import collections
import heapq

class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        directions = [
            [0,1, True],
            [1,0, True],
            [-1, 0, False],
            [0,-1, False]
        ]

        minHeap = [(1, 0, 0, True)] # cost, row, col, is_odd
        seen = collections.defaultdict(int)
        seen[(0, 0, True)] = 1 # row, col, is_odd

        while minHeap:
            cost, row, col, is_odd = heapq.heappop(minHeap)

            if row == m-1 and col == n-1:
                return cost

            if cost > seen.get((row, col, is_odd), float('inf')):
                continue

            new_is_odd = not is_odd

            # choose to move
            for dr, dc, curr_odd in directions:
                xr, xc = row + dr, col + dc
                if xr in range(m) and xc in range(n):
                    new_cost = (xr+1) * (xc+1)
                    new_cost += cost
                    if curr_odd != is_odd:
                        new_cost += penalty[row][col]
                    if new_cost < seen.get((xr, xc, new_is_odd), float('inf')):
                        seen[(xr, xc, new_is_odd)] = new_cost
                        heapq.heappush(minHeap, (new_cost, xr, xc, new_is_odd))

            # choose to stay
            wait_cost = cost + penalty[row][col]
            if wait_cost < seen.get((row, col, new_is_odd), float('inf')):
                seen[(row, col, new_is_odd)] = wait_cost
                heapq.heappush(minHeap, (wait_cost, row, col, new_is_odd))


        return -1
