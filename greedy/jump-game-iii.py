class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        seen = set()

        def f(index):
            if arr[index] == 0:
                return True
            if index in seen:
                return False

            left, right = False, False
            seen.add(index)

            if (index - arr[index]) >= 0:
                left = f(index-arr[index])
            if (index + arr[index]) < len(arr):
                right = f(index + arr[index])

            return left or right
        return f(start)
