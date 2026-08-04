import collections
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        """
        "@...a",
        ".###A"
        "b.BCc"
        """
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        seen = set() #row, col, mask

        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        target = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "@":
                    queue.append((0,0,i,j)) # steps, key_mask, row, col
                    seen.add((i, j, 0)) #  row, col, mask

                else:
                    c = grid[i][j]
                    if c.isalpha() and c.islower():
                        target |= 1 << (ord(c) - ord('a'))


        while queue:
            steps, mask, r, c = queue.popleft()

            if target == mask:
                return steps

            for dr, dc in directions:
                xr, xc = dr+r, dc+c
                if not (0 <=xr <rows and 0 <= xc < cols):
                    continue
                char = grid[xr][xc]

                if char == "#":
                    continue

                newMask = mask
                if char.islower():
                    newMask |= 1 << (ord(char) - ord('a'))

                if char.isupper():
                    if not (newMask & (1 << (ord(char.lower()) - ord('a')))):
                        continue
                if (xr, xc, newMask) in seen:
                    continue
                seen.add((xr, xc, newMask))
                queue.append((steps+1, newMask, xr, xc))

        return -1
