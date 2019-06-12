class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        N = len(s)
        steps = [1, 2, 3]
        
        def dfs(st, path, depth):
            # max depth
            if depth == 4:
                if st == N:
                    res.append(path[1:])
                return
            
            # depth < 4 and reach the end
            if st >= N:
                return
            
            # special case: 0 at the head of substring
            if s[st] == '0':
                dfs(st + 1, path + '.0', depth + 1)
                return
            
            # other case
            for step in steps:
                ed = st + step
                if ed > N:
                    break
                sub = s[st:ed]
                if int(sub) <= 255:
                    dfs(ed, path + '.' + sub, depth + 1)
                    
        dfs(0, "", 0)
        return res