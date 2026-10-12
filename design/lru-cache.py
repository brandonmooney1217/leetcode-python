class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dct = {}

    def insert(self, node):
        prev = self.tail.prev

        node.prev = prev
        node.next = self.tail

        self.tail.prev = node
        prev.next = node


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1
        else:
            node = self.dct[key]
            self.remove(node)
            self.insert(node)
            return node.val



    def put(self, key: int, value: int) -> None:

        if key in self.dct:
            self.remove(self.dct[key])
            del self.dct[key]

        node = ListNode(key, value)
        self.dct[key] = node
        self.insert(node)

        if len(self.dct) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.dct[lru.key]




        """
       (1 1) (3,3)
        """








# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
