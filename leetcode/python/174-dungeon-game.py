'''
由右下(P)往左上建，原則:每一格所存的是由"該格"走到"最後"所需要的最少血量
注意邊界初始
'''

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        
        # 0 for acc, 1 for burden
        table = [[99999 for i in range(n+1)] for j in range(m+1)]
        table[m][n-1] = 1
        table[m-1][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                table[i][j] = max(1, min(table[i][j+1], table[i+1][j])-dungeon[i][j])
        return table[0][0]