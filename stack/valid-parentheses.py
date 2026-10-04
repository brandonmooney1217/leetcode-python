# LeetCode #20 (Easy): https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['(', '{', '[']
        closed = [')', '}', ']']
        stack = []

        for c in s:
            if c in opened:
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False



        return len(stack) == 0
