# LeetCode #57 (Medium): https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        index = 0

        while index < len(intervals) and newInterval[0] > intervals[index][1]:
            res.append(intervals[index])
            index +=1

        start = newInterval[0]
        end = newInterval[1]

        while index < len(intervals) and end >= intervals[index][0]:
            start = min(start, intervals[index][0])
            end = max(end, intervals[index][1])
            index +=1
        res.append([start, end])


        while index < len(intervals):
            res.append(intervals[index])
            index +=1
        return res
