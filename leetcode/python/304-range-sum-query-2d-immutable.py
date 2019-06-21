class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        if not len(matrix) or not len(matrix[0]):
            return None
        
        N = len(matrix)
        M = len(matrix[0])
        
        
        self.table = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(M):
                self.table[i+1][j+1] = matrix[i][j] + \
                               self.table[i][j+1] + \
                               self.table[i+1][j] - \
                               self.table[i][j]
       
                
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.table[row2+1][col2+1] - \
               self.table[row2+1][col1] - \
               self.table[row1][col2+1] + \
               self.table[row1][col1]
