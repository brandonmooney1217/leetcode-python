class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        seen = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols):
                return False
            if grid[r][c] == 1:
                return True

            tmp = True
            for dr, dc in directions:
                xr, xc = dr+r, dc+c
                if (xr, xc) not in seen:
                    seen.add((xr,xc))
                    tmp &= dfs(xr, xc)

            return tmp


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r,c) not in seen:
                    seen.add((r,c))
                    tmp = dfs(r,c)
                    if tmp:
                        count +=1

        return count


        """
        [0,0,1,1,0,1,0,0,1,0],
        [1,1,0,1,1,0,1,1,1,0],
        [1,0,1,1,1,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,1,1,0],
        [0,1,0,1,0,1,0,1,1,1],
        [1,0,1,0,1,1,0,0,0,1],
        [1,1,1,1,1,1,0,0,0,0],
        [1,1,1,0,0,1,0,1,0,1],
        [1,1,1,0,1,1,0,1,1,0]
        """
