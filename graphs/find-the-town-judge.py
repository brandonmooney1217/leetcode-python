class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = 0
        outdegree = [0] * (n+1)
        dct = collections.defaultdict(list)

        for a, b in trust:
            outdegree[a] +=1
            dct[b].append(a)

        queue = collections.deque()
        for i in range(1, n+1):
            val = outdegree[i]
            if val == 0:
                queue.append(i)

        if len(queue) == 0:
            return -1
        if len(queue) > 1:
            return -1

        res = queue[0]

        if len(dct[res]) != n-1:
            return -1

        return res
