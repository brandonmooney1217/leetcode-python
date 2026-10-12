class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.copy = nums.copy()
        self.length = len(self.nums)

    def reset(self) -> list[int]:
        self.nums[:] = self.copy
        return self.nums



    def shuffle(self) -> list[int]:
        arr = self.nums
        for i in range(self.length):
            random = randint(i, self.length-1)
            arr[i], arr[random] = arr[random], arr[i]
        return arr




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
