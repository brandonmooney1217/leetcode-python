class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = []

        for x, y in points:
            dst = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, (dst, x, y))

        res = []
        while k and minHeap:
            _, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        return res
