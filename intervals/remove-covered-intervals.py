# LeetCode #1288 (Medium): https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        count = 0

        intervals.sort(key = lambda x :(x[0], x[1]*-1))

        l, r = intervals[0][0], intervals[0][1]

        for i in range(1, n):
            curr_l, curr_r = intervals[i]
            if l <= curr_l and r >= curr_r:
                count +=1
            else:
                l, r = curr_l, curr_r

        return n-count
