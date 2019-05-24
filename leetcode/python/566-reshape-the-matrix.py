class Solution(object):
    def matrixReshape(self, nums, r, c):
        n = len(nums[0])
        try:
            new = [[nums[(i*c+j)//n][(i*c+j)%n] for j in range(c)] for i in range(r)]
            return new
        except:
            return nums