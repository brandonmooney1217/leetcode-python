
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = []
        for l, r in flowers:
            events.append((l, 1))
            events.append((r+1, -1))
        events.sort()
        print(events)

        ppl = []
        for index, val in enumerate(people):
            ppl.append((val, index))
        ppl.sort()
        dct = {}
        coverage, event_index = 0, 0

        for time, index in ppl:
            while event_index < len(events) and events[event_index][0] <=time:
                coverage += events[event_index][1]
                event_index +=1
            dct[index] = coverage
        res = [0] * len(people)
        for key, val in dct.items():
            res[key] = val
        return res
