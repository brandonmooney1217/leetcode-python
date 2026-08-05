from typing import List
import collections

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0] * n
        dct = collections.defaultdict(set)

        for src, dst in roads:
            indegree[src] +=1
            indegree[dst] +=1
            dct[src].add(dst)
            dct[dst].add(src)
        tmp = []
        for i in range(n):
            tmp.append([indegree[i], i])

        res = 0

        for i in range(len(tmp)):
            for j in range(i+1, len(tmp)):
                t1 = tmp[i]
                t2 = tmp[j]

                count = t1[0] + t2[0]
                if t1[1] in dct[t2[1]]:
                    count -=1
                res = max(res, count)
        return res
