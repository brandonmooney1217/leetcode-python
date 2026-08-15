class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mx = max(b, a)
        mn = min(a, b)

        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        lcm = mx / gcd(a, b) * mn

        left, right = 1, mn * n

        while left < right:
            mid = (left+right) //2
            count = (mid//mn) + (mid//mx) - (mid//lcm)

            if count < n:
                left = mid + 1
            else:
                right = mid
        return left % (10**9 + 7)
