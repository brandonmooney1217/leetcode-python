from typing import List
import collections

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        dct = collections.defaultdict(list)
        n = len(graph)
        in_degree = [0 for _ in range(n)]

        for index, val in enumerate(graph):
            in_degree[index] += len(val)
            for v in val:
                dct[v].append(index)
        print(in_degree)
        print(dct)
        queue = collections.deque()
        for index, val in enumerate(in_degree):
            if val == 0:
                queue.append(index)

        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)

            for nei in dct[curr]:
                in_degree[nei] -=1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return sorted(res)
