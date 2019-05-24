class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        max_reach = nums[0]
        i = 0
        last = len(nums) - 1
        
        while i <= max_reach and i < last:
            max_reach = max(max_reach, i+nums[i])
            i += 1
        
        return  max_reach >= last