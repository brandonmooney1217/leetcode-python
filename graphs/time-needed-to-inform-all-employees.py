from typing import List
import collections

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        res = 0
        dct = collections.defaultdict(list)

        for index, val in enumerate(manager):
            if val == -1: continue
            dct[val].append(index)

        queue = collections.deque()
        queue.append((0, headID))

        while queue:
            time, node = queue.popleft()
            res = max(res, time)
            time2 = informTime[node]

            for nei in dct[node]:
                queue.append((time2+time, nei))
        return res
