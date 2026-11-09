class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack = [] # index, height
        res = 0

        for i in range(n):
            curr_height = heights[i]
            mn_index = i

            while stack and curr_height < stack[-1][1]:
                mn_index, mn_height = stack.pop()
                res = max(res, mn_height * (i-mn_index))

            stack.append([mn_index, curr_height])
        for i in range(len(stack)-1, -1, -1):
            curr_index, curr_height = stack[i]
            res = max(res, curr_height * (n-curr_index))
        return res
