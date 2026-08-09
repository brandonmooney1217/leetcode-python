from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0

    def find(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.count +=1
        elif self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 != p2:
            self.parent[p2] = self.parent[p1]
            self.count -=1


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind()

        for s in strs:
            uf.find(s)

        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                s1, s2 = strs[i], strs[j]
                count = 0
                for c1, c2 in zip(s1, s2):
                    if c1 != c2:
                        count +=1
                # strings are similar if they have 2 or 0 mismatches; they are always anagrams
                if count == 2 or count == 0:
                    uf.union(s1, s2)

        return uf.count
