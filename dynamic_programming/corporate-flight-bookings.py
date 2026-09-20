class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        tmp = [0] * (n+1)

        for start, end, val in bookings:
            tmp[start-1] += val
            tmp[end] -=val

        prefix = [0]
        for val in tmp:
            prefix.append(prefix[-1] + val)
        return prefix[1:n+1]
