class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(spells)
        res = [0] * n

        def bs(value):
            l, r = 0, len(potions)

            while l < r:
                mid = (l+r) //2
                power = value * potions[mid]

                if power < success:
                    l = mid+1
                else:
                    r = mid
            return len(potions)-l

        for index, val in enumerate(spells):
            tmp = bs(val)
            res[index] = tmp

        return res
