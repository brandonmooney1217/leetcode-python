import collections

class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:

        dct = collections.defaultdict(set)
        for s, d in roads:
            dct[s].add(d)
            dct[d].add(s)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                i_count = len(dct[i])
                j_count = len(dct[j])
                count = i_count + j_count

                if i in dct[j] or j in dct[i]:
                    count-=1
                res = max(res, count)
        return res
