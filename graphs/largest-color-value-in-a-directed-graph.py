import collections
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        dct = collections.defaultdict(list)
        color_dct = {}
        indegree = [0] * n
        for src, dst in edges:
            indegree[dst] +=1
            dct[src].append(dst)

        for i in range(n):
            color_dct[i] = [0] * 26
            c = ord(colors[i]) - ord('a')
            color_dct[i][c] +=1

        queue = collections.deque()
        visited = 0
        res = 0
        for index, val in enumerate(indegree):
            if val == 0:
                queue.append(index)

        while queue:
            curr = queue.popleft()
            visited +=1
            res = max(res, max(color_dct[curr]))

            for nei in dct[curr]:
                indegree[nei] -=1
                for i in range(26):
                    color_dct[nei][i] = max(color_dct[nei][i], color_dct[curr][i] + (i == ord(colors[nei]) - ord('a')))

                if indegree[nei] == 0:
                    queue.append(nei)

        return res if visited == n else -1
