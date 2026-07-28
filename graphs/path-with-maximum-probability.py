from typing import List
import collections
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = collections.defaultdict(list)
        for edge, prob in zip(edges, succProb):
            a, b = edge
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        minHeap = [(-1, start_node)]
        seen = {}
        seen[start_node] = 1

        while minHeap:
            neg_prob, node = heapq.heappop(minHeap)
            pos_prob = neg_prob * -1

            if node == end_node:
                return pos_prob

            if pos_prob < seen.get(node, float('-inf')):
                continue

            for nei, nei_prob in graph[node]:
                new_prob = nei_prob * pos_prob

                if new_prob > seen.get(nei, float('-inf')):
                    seen[nei] = new_prob

                    heapq.heappush(minHeap, (-new_prob, nei))
        return 0
