
from typing import List
import collections
from collections import Counter

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        dct = collections.defaultdict(list)
        n = len(graph)
        res = []
        path = []

        for index, val in enumerate(graph):
            for v in val:
                dct[index].append(v)

        def f(node):
            path.append(node)
            if node == n-1:
                res.append(path[:])
            else:
                for nei in dct[node]:
                    f(nei)
            path.pop()
        f(0)
        return res
