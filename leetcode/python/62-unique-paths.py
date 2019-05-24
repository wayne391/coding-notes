class Solution:
    def uniquePaths(self, m, n):
        lookup = [[1]*m]
        lookup.extend([[1]+[0]*(m-1) for _ in range(n-1)])
        for i in range(1, n):
            for j in range(1, m):
                lookup[i][j] = lookup[i][j-1] + lookup[i-1][j]
        return lookup[n-1][m-1]
