class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix: return
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0]*n for _ in range(m)]
        self.prefix[0][0] = matrix[0][0]
        for i in range(1, n): self.prefix[0][i] = self.prefix[0][i-1] + matrix[0][i]
        for j in range(1, m): self.prefix[j][0] = self.prefix[j-1][0] + matrix[j][0]
        for i in range(1, m):
            for j in range(1, n):
                self.prefix[i][j] = self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1] + matrix[i][j]
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]
        if row1 > 0:
            total -= self.prefix[row1-1][col2]
        if col1 > 0:
            total -= self.prefix[row2][col1-1]
        if col1 > 0 and row1 > 0:
            total += self.prefix[row1-1][col1-1]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)