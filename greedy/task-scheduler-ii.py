# LeetCode #2365 (Medium): https://leetcode.com/problems/task-scheduler-ii/
from typing import List

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        dct = {}
        time = 0

        for task in tasks:
            time = max(time+1, dct.get(task, 0))
            dct[task] = time + space + 1
        return time
