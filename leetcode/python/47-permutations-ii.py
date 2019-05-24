class Solution:
    def permuteUnique(self, nums):
        self.collect = []
        self.permutation(sorted(nums), [])
        return self.collect

    def permutation(self, nums, result):
        if len(nums) == 1:
            self.collect.append(result+nums)
            return

        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n-1]:
                continue

            tmp = nums[:]
            tmp[n:n+1] = ()
            self.permutation(tmp, result+[nums[n]])
