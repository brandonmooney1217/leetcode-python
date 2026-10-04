# LeetCode #856 (Medium): https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        interate through each char of s
            - if open, add 1 to multipliter
            - if close, subtract from multiplier
                - add to sm - multiplier-1 * 2
        """

        tmp = 0
        sm = 0
        canMultiply = False

        for c in s:
            if c == "(":
                tmp +=1
                canMultiply = True
            else:
                if canMultiply:
                    sm += (2**(tmp-1))
                canMultiply = False
                tmp-=1

        return sm
