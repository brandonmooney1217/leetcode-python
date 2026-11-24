class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.dp = [[0 for _ in range(self.cols + 1)] for _ in range(self.rows+1)]

        for i in range(self.rows):
            for j in range(self.cols):
                self.dp[i+1][j+1] = self.matrix[i][j] + self.dp[i+1][j] + self.dp[i][j+1] - self.dp[i][j]
        print(self.dp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]

    """
    [0, 0, 0,  0,  0,   0],
    [0, 3, 3,  4,  8,  10],
    [0, 8, 14, 18, 24, 27],
    [0, 9, 17, 21, 28, 36],
    [0, 13, 22,26, 34, 49],
    [0, 14, 23,30, 38, 58]]

    BLUE
    (1,2) (2,4)
    (2,3) (3,4)

    GREEN
    (1,1) (2,2)
    (2,2) (3,3)

    21 -   4 -   9 +   3
    (3,3). (1,3) (3,1) (1,1)
    dp[row2+1][col2+1] -

    """




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
