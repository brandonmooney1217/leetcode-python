class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        length = len(rides)

        def binary_search(end):
            l, r = 0, length

            while l < r:
                mid = (l+r) //2
                if rides[mid][0] < end:
                    l = mid+1
                else:
                    r = mid
            return l
        @cache
        def dp(index):
            if index >= length:
                return 0

            skip = dp(index+1)

            start, end, tip = rides[index]
            next_index = binary_search(end)
            profit = (end-start) + tip

            take = dp(next_index) + profit
            return max(skip, take)
        return dp(0)
