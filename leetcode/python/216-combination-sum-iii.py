class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        vis_map = [False for _ in range(10)]
        
        def dfs(remain, start, level, vis, path):
            if level == (k+1) and remain == 0:
                res.append(path)
                return
            if level > k:
                return
     
            for i in range(start, 10):
                if remain < i:
                    break
                if not vis[i]:
                    tmpv = vis[:]
                    tmpv[i] = True
                    dfs(remain - i, i + 1, level + 1, tmpv, path + [i])
                
        dfs(n, 1, 1, vis_map, [])
            
        return res