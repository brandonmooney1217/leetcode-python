from typing import List
import collections

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]

        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        queue = collections.deque()
        seen = set()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    seen.add((i, j))

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                xr, xc = dr+r, dc+c

                if xr >= 0 and xr < rows and xc >=0 and xc < cols:
                    if (xr, xc) not in seen and mat[xr][xc] == 1:
                        seen.add((xr, xc))
                        res[xr][xc] = res[r][c] + 1
                        queue.append((xr,xc))
        return res
