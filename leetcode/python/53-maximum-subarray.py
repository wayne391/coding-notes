class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        max_sum = cum_sum = nums[0]
        for i in range(1, len(nums)):
            cum_sum = max(nums[i], nums[i]+cum_sum)    
            if max_sum < cum_sum:
                max_sum = cum_sum
        return max_sum