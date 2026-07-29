from typing import List
import collections
import heapq
from functools import cache

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        dist = [float('inf') for _ in range(n+1)]
        dist[n] = 0

        minHeap = [[0,n]]
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if cost > dist[node]:
                continue

            for nei, nei_weight in graph[node]:
                new_weight = nei_weight + cost

                if new_weight < dist[nei]:
                    dist[nei] = new_weight
                    heapq.heappush(minHeap, [new_weight, nei])
        @cache
        def dfs(node):
            if node == n:
                return 1
            count = 0
            for nei, _ in graph[node]:
                if dist[node] > dist[nei]:
                    count = (dfs(nei) + count) % (10**9+7)
            return count
        return dfs(1)
