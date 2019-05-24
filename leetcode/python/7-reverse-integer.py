class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = str(abs(x))
        x_ = x[::-1]
        result = int(x_)*sign
        ans = result if (result > -2**31) and (result < 2**31) else 0
        return ans
