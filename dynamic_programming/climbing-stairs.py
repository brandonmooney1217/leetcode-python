class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=3:
            return n

        t1, t2 = 1, 1
        for _ in range(2, n+1):
            tmp = t2
            t2 = t2 + t1
            t1 = tmp
        return t2
