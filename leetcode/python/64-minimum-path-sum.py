class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        lookup = grid[:]
        for j in range(1, n):
            lookup[0][j] = grid[0][j] + grid[0][j-1]
        for i in range(1, m):
            lookup[i][0] = grid[i][0] + grid[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                lookup[i][j] = min(
                        lookup[i][j]+lookup[i][j-1],
                        lookup[i][j]+lookup[i-1][j]
                        )
        return lookup[m-1][n-1]
