class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        key insight is that we want to test the values and not the indexes
        i.e i m or n

        the answer is somewhere between 1 and m*n, so we do Binary search on this range
        once we have a value to test, we can look at each row and see how numbers in that row are
        below the test value

        each row contains values 1i, 2i, 3i ... where represents that row
        therefore, the num of values below target is equal test // row

        """

        l, r = 1, m*n

        while l < r:
            mid = (l+r) //2
            count = 0

            for i in range(1, m+1):
                count += min(n, mid//i)

            if count < k:
                l = mid+1
            else:
                r = mid
        return l
