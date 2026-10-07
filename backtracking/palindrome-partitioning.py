class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        curr = []

        def f(index):
            if index == len(s):
                res.append(curr[:])
                return

            for i in range(index, len(s)):
                curr_string = s[index:i+1]
                if curr_string[::-1] == curr_string:
                    curr.append(curr_string)
                    f(i+1)
                    curr.pop()
        f(0)
        return res
