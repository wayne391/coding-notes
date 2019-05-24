
class Solution:
    def permute(self, nums):
        self.collect = []
        self.permutation(nums, [])
        return self.collect

    def permutation(self, nums, result):
        if len(nums) == 1:
            self.collect.append(result+nums)
            return

        for n in range(len(nums)):
            tmp = nums[:]
            tmp[n:n+1] = ()
            self.permutation(tmp, result+[nums[n]])
