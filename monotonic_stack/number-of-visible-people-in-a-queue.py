class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:

        """
        [0 1 2 3]
         3  2  1 0

x


        """
        n = len(heights)
        res = [0] * n

        queue = collections.deque()
        queue.append(n-1)

        for i in range(n-2, -1, -1):
            count = 0
            while queue and heights[i] >= heights[queue[-1]]:
                queue.pop()
                count +=1
            if not queue:
                res[i] = count
            else:
                res[i] = count + 1
            queue.append(i)
        return res
