class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        # add to maxheap by default
        heapq.heappush(self.maxHeap, num * -1)

        # check if head of max greate than head of min
        if self.maxHeap and self.minHeap and (self.maxHeap[0] * -1 > self.minHeap[0]):
            val = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, val)

        # balance
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1*val)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] + (self.maxHeap[0] * -1)) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
