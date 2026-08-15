class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        mx = position[-1]
        mn = position[0]

        def feasible(test):
            count = 1
            prev = position[0]
            for i in range(1, len(position)):
                if position[i]-prev >= test:
                    prev = position[i]
                    count +=1
            return count >=m

        l, r = 1, mx-mn
        res = 0
        while l < r:
            mid = (l+r+1) //2
            if feasible(mid):
                l = mid
            else:
                r = mid-1
        return l
