from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 != p2:
            self.parent[p2] = self.parent[p1]
            return True
        else:
            return False

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        count = n
        for i in range(len(isConnected)):
            entry = isConnected[i]
            for index, val in enumerate(entry):
                if index == i:
                    continue
                else:
                    if val == 1:
                        count -= uf.union(i, index)
        return count
