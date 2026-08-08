
from typing import List
import collections

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dct = collections.defaultdict(list)
        for a, b in dislikes:
            dct[a].append(b)
            dct[b].append(a)
        print(dct)
        color = {}
        def dfs(node, c):
            color[node] = c
            for nei in dct[node]:
                if nei not in color:
                    if not dfs(nei, 1-c):
                        return False

                elif color[nei] == c:
                    return False
            return True

        for i in range(1, n+1):
            if i not in color:
                tmp = dfs(i, 1)
                print(i, tmp)
                if not tmp:
                    return False
        return True
