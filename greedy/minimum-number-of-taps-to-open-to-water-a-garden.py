class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        arr = []

        for i in range(len(ranges)):
            curr = ranges[i]
            left, right = max(0, i-curr), min(n, i + curr)
            arr.append([left, right])

        arr.sort(key = lambda x: (x[0], -x[1]))
        index = 0
        frontier = 0
        furthest = 0
        taps = 0

        while frontier < n:
            while index < len(arr) and arr[index][0] <= frontier:
                furthest = max(furthest, arr[index][1])
                index +=1
            if frontier == furthest:
                return -1
            taps +=1
            frontier = furthest
        return taps
