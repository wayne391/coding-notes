class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        str_s = []
        for ch in S:
            if ch == '#':
                if len(str_s):
                    str_s.pop(-1)
            else:
                str_s.append(ch)
                
        str_t = []
        for ch in T:
            if ch == '#':
                if len(str_t):
                    str_t.pop(-1)
            else:
                str_t.append(ch)
        return str_s == str_t