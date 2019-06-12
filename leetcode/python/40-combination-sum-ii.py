
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(candidates)
        vis_map = [False for n in candidates] 
        candidates.sort()
        
        def dfs(remain, vis, start, path):
            if remain == 0:
                res.append(path)
            else:
                prev = None
                for idx in range(start, N):
                    c = candidates[idx]
                    if c > remain:
                        break
                        
                    if vis[idx]:
                        continue
                        
                    if prev == c:
                        continue
                    else:
                        prev = c
                        if not vis[idx]:
                            tmpv = vis[:]
                            tmpv[idx] = True
                            dfs(remain - c, tmpv, idx, path + [c])
                        
        dfs(target, vis_map, 0, [])
        return res