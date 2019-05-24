class NumArray(object):
    def __init__(self, nums):
        self.acc = [0]
        for n in nums:
            self.acc.append(self.acc[-1]+n)
                
    def sumRange(self, i, j):
        return self.acc[j+1] - self.acc[i]