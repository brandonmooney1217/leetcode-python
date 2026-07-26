from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_times = [float('inf') for _ in range(n+1)]
        min_times[k] = 0

        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v,w))

        minHeap = [(0, k)]

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            print(node)

            if cost > min_times[node]:
                continue

            for nei, nei_cost in graph[node]:
                new_cost = cost + nei_cost
                if new_cost < min_times[nei]:
                    min_times[nei] = new_cost
                    heapq.heappush(minHeap, (new_cost, nei))
        tmp = max(min_times[1:])
        return tmp if tmp!=float('inf') else -1
