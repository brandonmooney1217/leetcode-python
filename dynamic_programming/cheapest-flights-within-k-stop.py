from typing import List
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = collections.defaultdict(list)
        for f, t, price in flights:
            graph[f].append((t, price))

        minPrice = [[float('inf') for _ in range(k+2)] for _ in range(n)]
        minPrice[src][0] = 0

        init_cost, init_stops = 0, 0
        minHeap = [(init_cost, init_stops, src)]

        while minHeap:
            curr_cost, curr_stops, curr_node = heapq.heappop(minHeap)

            if curr_node == dst:
                return curr_cost

            if curr_cost > minPrice[curr_node][curr_stops]:
                continue

            for nei, nei_cost in graph[curr_node]:
                nei_stops = curr_stops + 1
                nei_cost = curr_cost + nei_cost

                if nei_stops <=k+1 and nei_cost < minPrice[nei][nei_stops]:
                    minPrice[nei][nei_stops] = nei_cost
                    heapq.heappush(minHeap, (nei_cost, nei_stops, nei))
        return -1
