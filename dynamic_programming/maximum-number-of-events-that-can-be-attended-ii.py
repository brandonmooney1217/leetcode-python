class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        sort the events by start time

        state is just (left, index), which is number of moves left and the current index
            - at each pos we can either skip or take
                - if we take, then use binary search to find next valid pos


        """
        events.sort() # sort by start time
        n = len(events)

        def binary_search(end):
            l, r = 0, n

            while l < r:
                mid = (l+r)//2
                if events[mid][0] <= end:
                    l = mid+1
                else:
                    r = mid
            return l

        @cache
        def dp(index, count):
            if count == 0 or index >=n:
                return 0

            # skip value
            skip = dp(index+1, count)

            _, end, val = events[index]
            next_index = binary_search(end)

            take = val + dp(next_index, count-1)
            return max(take, skip)

        return dp(0, k)
