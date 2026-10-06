class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        rows, cols = len(board), len(board[0])
        seen = set()

        def dfs(r, c, index):
            if index == len(word):
                return True

            if r not in range(rows) or c not in range(cols):
                return False

            if (r,c) in seen:
                return False

            if board[r][c] != word[index]:
                return False
            seen.add((r,c))

            for dr, dc in directions:
                xr, xc = r + dr, c + dc
                if dfs(xr, xc, index+1):
                    return True

            seen.remove((r,c))
            return False
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
