'''
Bottom up
Key of speeding up:
    * 不要用python3 leetcode的input
    * 從小的開始

'''

class Solution(object):
    def combinationSum4(self, nums, target):
        if not nums: return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(min(nums), target+1):
            for n in nums: 
                if i >= n: dp[i] += dp[i - n]
        return dp[-1]


'''
My original: Top down
'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        
        dp = [0] * (target + 1)
        dp[-1] = 1
        
        for i in range(target, -1, -1):
            for n in nums:
                tmp = i + n
                if tmp <= target and dp[tmp]:    
                    dp[i] += dp[tmp]
        return dp[0]