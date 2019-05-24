class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        j = i = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i