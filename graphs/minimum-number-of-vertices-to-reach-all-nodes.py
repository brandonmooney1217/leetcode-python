from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for _, dst in edges:
            indegree[dst] +=1
        res = []
        for index, val in enumerate(indegree):
            if val == 0:
                res.append(index)
        return res
