'''
1. b xor 0 = b (XOR 自己是自己)
2. b xor b = 0 (自己XOR自己是0)
3. 交換律
'''
class Solution(object):
    def singleNumber(self, nums):
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res
        