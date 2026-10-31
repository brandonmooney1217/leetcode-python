# LeetCode #828 (Hard): https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        left = [0] * n
        right = [0] * n

        seen = {}
        for i in range(n):
            if s[i] not in seen:
                left[i] = i+1
            else:
                last_index = seen[s[i]]
                left[i] = i-last_index

            seen[s[i]] = i

        seen = {}
        for i in range(n-1, -1, -1):
            if s[i] not in seen:
                right[i] = n-i
            else:
                last_index = seen[s[i]]
                right[i] = last_index-i
            seen[s[i]] = i


        res = 0
        for l, r in zip(left, right):
            res += l*r
        return res
