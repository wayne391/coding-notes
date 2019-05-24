class Solution:
    def longestCommonPrefix(self, m):
        if not m: return ''
				#since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
        
#         N = len(strs)
#         idx = 0
#         ans = ""
        
#         while True:
#             if idx >= len(strs[0]):
#                 break
            
#             char = strs[0][idx]
#             for n in range(N):
#                 if idx >= len(strs[n]):
#                     return ans
                
#                 if (char != strs[n][idx]):
#                     return ans
#             ans += char
#             idx += 1
#         return ans
            