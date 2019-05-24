class Solution(object):
    def judgeCircle(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

# class Solution(object):
#     def judgeCircle(self, moves):
#         init = [0, 0]
#         step = {'U': (1, 0),'D': (-1, 0), 'L':(0, -1), 'R':(0, 1)}
#         for m in moves:
#             s = step[m]
#             init[0] += s[0]
#             init[1] += s[1]
#         return init == [0, 0]
