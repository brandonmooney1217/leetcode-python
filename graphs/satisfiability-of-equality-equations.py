from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, node):
        if node not in self.parent:
            self.parent[node] = node
        elif self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 != p2:
            self.parent[p2] = self.parent[p1]
            return True
        else:
            return False

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        for e in equations:
            a = e[0]
            b = e[3]
            val = e[1]
            if val == "=":
                uf.union(a, b)
        for e in equations:
            a = e[0]
            b = e[3]
            val = e[1]
            if val == "!":
                if uf.find(a) == uf.find(b):
                    return False
        return True
