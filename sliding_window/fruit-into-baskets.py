class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        l = 0
        dct = collections.defaultdict(int)

        for r in range(len(fruits)):
            fruit = fruits[r]
            dct[fruit] +=1


            while l < r and len(dct.keys()) > 2:
                dct[fruits[l]] -=1
                if dct[fruits[l]] == 0:
                    del dct[fruits[l]]
                l +=1
            res = max(res, r-l+1)

        return res
