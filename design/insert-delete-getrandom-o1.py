class RandomizedSet:

    def __init__(self):
        self.dct = {}
        self.arr = []


    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False

        self.arr.append(val)
        self.dct[val] = len(self.arr)-1
        return True


    def remove(self, val: int) -> bool:
        if val not in self.dct:
            return False

        last = self.arr[-1]
        last_index = self.dct[last]

        curr_index = self.dct[val]
        self.arr[curr_index], self.arr[last_index] = self.arr[last_index], self.arr[curr_index]
        self.dct[last] = curr_index

        del self.dct[self.arr[-1]]
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
