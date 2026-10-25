class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        rotten = 0
        total = 0
        time = -1
        queue = collections.deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh +=1
                total +=1
        if fresh == 0:
            return 0
        while queue:
            length = len(queue)
            for i in range(length):
                curr_row, curr_col = queue.popleft()
                rotten +=1

                for dr, dc in directions:
                    xr, xc = curr_row + dr, curr_col + dc
                    if xr not in range(rows) or xc not in range(cols):
                        continue
                    if grid[xr][xc] == 1:
                        grid[xr][xc] = 2
                        queue.append((xr, xc))
            time +=1
        return time if rotten == total else -1
