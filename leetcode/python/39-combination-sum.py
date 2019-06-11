'''
Fast solution
https://leetcode.com/problems/combination-sum/discuss/304571/Python-DFS-beats-99.76-(52ms-13.4-MB)
'''
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        
        def dfs(t, ind, path):
            if t == 0:
                res.append(path)
                return
            for i in range(ind, n):
                # 如果不夠湊則break
                # 因為有sort所以剩下不考慮
                # 沒有sort會慢不少
                if candidates[i] > t:
                    break
                dfs(t-candidates[i], i, path+[candidates[i]])
                
        dfs(target, 0, [])
        return res

'''
My original version, much slower
'''

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