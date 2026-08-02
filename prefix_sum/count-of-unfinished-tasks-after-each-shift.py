from typing import List

class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        """
        1 5 9
        9 1 4
        """
        n = len(tasks)
        prefix = [0]
        for task in tasks:
            prefix.append(prefix[-1] + task)
        total = prefix[-1]

        curr = 0
        res = []

        for shift in shifts:
            if curr + shift >= total:
                res.append(0)
                curr = 0
            else:
                curr += shift
                l, r = 0, len(prefix)-1
                while l < r:
                    mid = (l+r)//2
                    if prefix[mid] <= curr:
                        l = mid+1
                    else:
                        r = mid
                res.append(n-l+1)
        return res
