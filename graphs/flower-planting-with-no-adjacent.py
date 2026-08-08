from typing import List
import collections

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        dct = collections.defaultdict(list)
        for a, b in paths:
            dct[a].append(b)
            dct[b].append(a)

        res = [0] * (n+1)

        for node in range(1, n+1):
            used = set()
            for nei in dct[node]:
                if res[nei] != 0:
                    used.add(res[nei])

            for i in range(1,5):
                if i not in used:
                    res[node] = i
                    break

        return res[1:]
