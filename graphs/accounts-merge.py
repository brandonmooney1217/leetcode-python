
from typing import List
import collections

class UnionFind:
    def __init__(self):
        self.parent = {}
    def find(self, node):
        if node not in self.parent:
            self.parent[node] = node
        if self.parent[node] != node:
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            uf.find(first_email)
            email_to_name[first_email] = name
            for i in range(1, len(account)):
                curr_email = account[i]
                uf.union(first_email, curr_email)

        dct = collections.defaultdict(list)
        for key in uf.parent:
            parent = uf.find(key)
            dct[parent].append(key)

        res = []
        for key, val in dct.items():
            name = email_to_name[key]
            tmp = []
            for v in val:
                tmp.append(v)
            tmp.sort()
            tmp = [name] + tmp
            res.append(tmp)
        return res



    """
    {
    'johnsmith@mail.com': 'johnsmith@mail.com', 'john_newyork@mail.com': 'johnsmith@mail.com',

    'john00@mail.com': 'johnsmith@mail.com',

    'mary@mail.com': 'mary@mail.com',

    'johnnybravo@mail.com': 'johnnybravo@mail.com'}
    """
