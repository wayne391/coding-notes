class Solution(object):
    def hammingDistance(self, x, y):
        dist = 0
        while x or y:
            if x % 2 != y % 2:
                dist += 1
            x = x // 2
            y = y // 2
        return dist

'''
One line, The type of return value of 'bin' fuction is 'str'
'''
# class Solution(object):
#     def hammingDistance(self, x, y):
#         return bin(x^y).count('1')