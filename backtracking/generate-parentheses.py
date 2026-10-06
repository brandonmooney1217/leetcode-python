class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        curr = []
        res = []

        def f(opened, closed):
            if len(curr) == 2*n:
                res.append("".join(curr[:]))
                return
            if opened < n:
                curr.append("(")
                f(opened+1, closed)
                curr.pop()
            if closed < opened:
                curr.append(")")
                f(opened, closed+1)
                curr.pop()
        f(0, 0)
        return res
