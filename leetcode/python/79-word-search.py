class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        L = len(word)
        
        def dfs(i, j, cur):
            if not(0 <= i < M and 0 <= j < N):
                return False
            cur_char = board[i][j]
            if cur_char != word[cur]:
                return False
            if cur == (L -  1):
                return True
            board[i][j] = ''
            
            if dfs(i+1, j, cur + 1):
                return True
            if dfs(i, j+1, cur + 1):
                return True
            if dfs(i-1, j, cur + 1):
                return True
            if dfs(i, j-1, cur + 1):
                return True

            board[i][j] = cur_char
            return False
        
        for i in range(M):
            for j in range(N):
                if dfs(i, j, 0):
                    return True
        return False