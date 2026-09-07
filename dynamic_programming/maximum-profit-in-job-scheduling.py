class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        events = []

        for s, e, p in zip(startTime, endTime, profit):
            events.append([s, e, p])
        events.sort()
        n = len(events)
        print(events)

        def binary_search(end):
            l, r = 0, n

            while l < r:
                mid = (l+r) //2
                if events[mid][0] < end:
                    l = mid+1
                else:
                    r = mid
            return l

        @cache
        def dp(index):
            if index >= n:
                return 0

            skip = dp(index+1)
            start, end, prof = events[index]

            next_index = binary_search(end)
            take = dp(next_index) + prof

            return max(take, skip)
        return dp(0)
