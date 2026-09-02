class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for s, d, v in flights:
            graph[s].append((d,v))

        minPrice = [[float('inf') for _ in range(k+2)] for _ in range(n)]
        minPrice[src][0] = 0

        minHeap = [(0, 0, src)] # ccost, stops, node

        while minHeap:
            cost, stops, node = heapq.heappop(minHeap)
            if node == dst:
                return cost

            if cost > minPrice[node][stops]:
                continue

            for nei, nei_cost in graph[node]:
                nei_stops = stops+1
                nei_distance = cost + nei_cost

                if nei_stops <= k+1 and nei_distance < minPrice[nei][nei_stops]:
                    minPrice[nei][nei_stops] = nei_distance
                    heapq.heappush(minHeap, (nei_distance, nei_stops, nei))
        return -1
