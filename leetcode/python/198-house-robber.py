class Solution(object):
    def rob(self, nums):
        nums = [0, 0] + nums
        table = [0, 0]
        N = len(nums)
        for i in range(2, N):
            table.append(max(table[i-1], nums[i]+table[i-2]))
        return table[-1]