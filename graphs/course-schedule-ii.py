
import collections
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        dct = collections.defaultdict(list)

        for a, b in prerequisites:
            indegree[a] +=1
            dct[b].append(a)

        res = []
        queue = collections.deque()
        for index, val in enumerate(indegree):
            if val == 0:
                queue.append(index)

        while queue:
            curr = queue.popleft()
            res.append(curr)

            for nei in dct[curr]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
        return res if len(res) == numCourses else []
