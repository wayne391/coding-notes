'''
Recursion
'''
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        N = len(S)
        def dfs(string, index):
            if index == N:
                res.append(string)
                return
            char = S[index]
            if char.isalpha():
                dfs(string+char.lower(), index + 1)
                dfs(string+char.upper(), index + 1)
            else:
                dfs(string+char, index + 1)
        dfs("", 0)
        return res

'''
Iteration
'''

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        queue = [""]
        
        for ch in S:
            tmp_q = []
            flag = ch.isalpha()
                
            for q in queue:
                if flag:
                    tmp_q.append(q + ch.lower())
                    tmp_q.append(q + ch.upper())
                else: 
                    tmp_q.append(q + ch)
            queue = tmp_q
        return queue