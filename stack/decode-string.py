# LeetCode #394 (Medium): https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                curr_str = ""
                while stack and stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                stack.pop()
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num
                stack.append(int(curr_num) * curr_str)
        return "".join(stack)
