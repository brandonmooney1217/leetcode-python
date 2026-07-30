from typing import List
import collections

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)

        count = 0
        dct = collections.defaultdict(list)
        visited = set()
        visited.add(0)


        for index, val in enumerate(rooms):
            for v in val:
                if 0 == v: continue
                dct[index].append(v)
        queue = collections.deque()
        queue.append(0)

        while queue:
            curr = queue.popleft()
            count +=1

            for nei in dct[curr]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return count == n
