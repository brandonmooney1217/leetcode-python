from typing import List
import collections

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        count = 0

        queue = collections.deque()
        queue.append(0)
        visited = set()
        visited.add(0)

        while queue:
            curr = queue.popleft()
            count +=1
            for key in rooms[curr]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        return count == n
