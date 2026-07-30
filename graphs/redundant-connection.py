from typing import List

class UnionFind:
    def __init__ (self, n):
        self.parent = [i for i in range(n+1)]

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 != p2:
            self.parent[p2] = p1
            return True
        else:
            return False
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        uf = UnionFind(n)

        for x, y in edges:
            tmp = uf.union(x, y)
            if not tmp:
                return [x,y]
