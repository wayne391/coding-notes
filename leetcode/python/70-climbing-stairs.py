class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return n
        table = [1, 1]
        for i in range(n - 1):
            table.append(table[-1] + table[-2])
        return table[-1]