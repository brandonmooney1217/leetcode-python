# LeetCode #435 (Medium): https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """
        [[-73, -26], [-65, -11], [-63, 2], [-62, -49], [-52, 31], [-40, -26], [-31, 49], [30, 47], [58, 95], [66, 98], [82, 97], [95, 99]]

        [[-62, -49], [-73, -26], [-40, -26], [-65, -11], [-63, 2], [-52, 31], [30, 47], [-31, 49], [58, 95], [82, 97], [66, 98], [95, 99]]
        """
        intervals.sort(key=lambda x: x[1])
        count = 0

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if prev_end > curr_start:
                count +=1
            else:
                prev_end = curr_end
        return count
