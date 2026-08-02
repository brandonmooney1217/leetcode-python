
from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        events = []

        for s, e in ranges:
            events.append((s, 1))
            events.append((e+1, -1))
        events.sort()

        coverage, event_index = 0, 0
        for i in range(left, right+1):
            while event_index < len(events) and events[event_index][0] <=i:
                coverage += events[event_index][1]
                event_index +=1
            if coverage <=0:
                return False

        return True
