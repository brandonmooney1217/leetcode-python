class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:

        # sort by pairs with the largest difference
        tasks.sort(key = lambda x: -(x[1]-x[0]))

        count = 0
        res = 0

        for actual, mn in tasks:
            if count < mn:
                difference = mn-count
                res += difference
                count += difference
            count -=actual
        return res
