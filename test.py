def minPathSum(self, grid: List[List[int]]) -> int:
    
    for i in range(n-2, -1, -1): grid[m-1][i] += grid[m-1][i+1]
    for j in range(m-2, -1, -1): grid[j][n-1] += grid[j+1][n-1]
    if m == 1 or n == 1: return gird[0][0]
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            gird[i][j] += max(grid[i+1][j], grid[i][j+1])
    return grid[0][0]