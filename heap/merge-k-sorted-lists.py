# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        minHeap = []
        count = 0
        for head in lists:
            if head:
                heapq.heappush(minHeap, (head.val, count, head))
                count +=1

        res = ListNode(-1, None)
        tmp = res

        while minHeap:
            _, _, node = heapq.heappop(minHeap)
            tmp.next = node
            tmp = tmp.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, count, node.next))
                count +=1

        return res.next
