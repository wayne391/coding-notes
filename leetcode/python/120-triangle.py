'''
Bottom-Up, very quick!
'''
class Solution:
    def minimumTotal(self, tri: 'List[List[int]]') -> 'int':
        t = [0] * (len(tri[-1]) + 1)
        for level in tri[::-1]:
            for i in range(len(level)):
                t[i] = min(t[i], t[i+1]) + level[i]
        return t[0]

'''
Top-Down
'''
# class Solution:
#     def minimumTotal(self, tri: 'List[List[int]]') -> 'int':
#         for level in range(len(tri)):
#             if level == 0:
#                 table = [tri[0][0]]
#             else:
#                 N = len(tri[level])
#                 sub = []
#                 for i in range(N):
#                     if i == 0:
#                         sub.append(table[0]+tri[level][0])
#                     elif i == (N-1):
#                         sub.append(table[-1]+tri[level][-1])
#                     else:
#                         tmp = min(table[i-1], table[i])
#                         sub.append(tmp+tri[level][i])
#                 table = sub
#         return min(table)
