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
    def closedIsland2(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        seen = set()
        def fill(r,c):
            if r not in range(rows) or c not in range(cols):
                return
            if (r, c) in seen:
                return
            if grid[r][c] == 1:
                return
            grid[r][c] = 1
            seen.add((r,c))
            for dr, dc in directions:
                xr, xc = dr + r, dc + c
                fill(xr, xc)

        for r in range(rows):
            if grid[r][0] == 0:
                fill(r, 0)
            if grid[r][cols-1] == 0:
                fill(r, cols-1)

        for c in range(cols):
            if grid[0][c] == 0:
                fill(0, c)
            if grid[rows-1][c] == 0:
                fill(rows-1, c)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r,c) not in seen:
                    fill(r,c)
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
