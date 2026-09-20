class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        """
        problem
            given clips array
            need to stitch them togther to cover entire time

            return min num of clips or -1 of impossoble

        impl
            sort the clips by start time, then -1 * end time?
            iterate through clips
                if curr start time > frontier, return -1
                else
        """
        clips.sort(key=lambda x: (x[0], -x[1]))
        frontier = 0
        furthest = 0
        index = 0
        res = 0

        while frontier < time:
            while index < len(clips) and clips[index][0] <= frontier:
                furthest = max(furthest, clips[index][1])
                index +=1

            if furthest == frontier:
                return -1

            frontier = furthest
            res +=1
        return res
