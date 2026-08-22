class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 10**9 + 7
        @cache
        def dfs(index, remain):
            count = 0
            if index == finish:
                count +=1

            for i in range(n):
                if i == index:
                    continue
                difference = abs(locations[index]-locations[i])
                if remain-difference >=0:
                    count = (count + dfs(i, remain-difference)) % MOD

            return count
        return dfs(start, fuel)
