# LeetCode #739 (Medium): https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and temperatures[stack[-1]] < curr:
                index = stack.pop()
                distance = i - index
                res[index] = distance
            stack.append(i)
        return res
