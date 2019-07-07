class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, string):
            if left > right:
                return
            elif not left and not right:
                res.append(string)
            else:
                if left > 0:
                    dfs(left - 1, right, string + '(')
                if right > 0:
                    dfs(left, right - 1, string + ')')    
        dfs(n, n, "")
        return res   