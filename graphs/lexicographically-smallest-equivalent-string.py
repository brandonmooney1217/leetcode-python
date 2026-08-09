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
        if p1 == p2:
            return

        if p1 < p2:
            self.parent[p2] = self.parent[p1]
        else:
            self.parent[p1] = self.parent[p2]

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for c1, c2 in zip(s1, s2):
            uf.union(c1, c2)
        res = []
        for c in baseStr:
            parent = uf.find(c)
            res.append(parent)
        print(uf.parent)
        return "".join(res)
