from typing import List
import collections


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        in_graph = collections.defaultdict(list)
        out_graph = collections.defaultdict(list)

        for src, dst in connections:
            out_graph[src].append(dst)
            in_graph[dst].append(src)

        queue = collections.deque() # node
        queue.append(0)

        seen = set()
        seen.add(0)

        while queue:
            curr = queue.popleft()

            for nei in in_graph[curr]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append(nei)
            for nei in out_graph[curr]:
                if nei not in seen:
                    seen.add(nei)
                    count +=1
                    queue.append(nei)

        return count
