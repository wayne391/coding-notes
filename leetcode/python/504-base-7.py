'''
Be care of the boundaries
'''
class Solution(object):
    def convertToBase7(self, num):
        if not num:
            return '0'
        out = ''
        neg = True if num < 0 else False
        num = abs(num)
        while num:
            mod = num % 7
            num = num // 7
            out += str(mod)
        out = out[::-1]
        if neg:
            out = '-'+ out
        return out 