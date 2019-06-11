class Solution:
    def dfs(self, cur_sum, start, path):
        if cur_sum == self.target:
            self.res.append(path)
            return
        elif cur_sum > self.target:
            return 
        else:
            for i in range(start, len(self.candidates)):
                temp = self.candidates[i]
                self.dfs(cur_sum+temp, i, path + [temp])
                
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.candidates = candidates
        self.target = target
        
        self.dfs(0, 0, [])
        return self.res