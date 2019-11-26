class Solution(object):
    def twoSum(self, nums, target):
        num_map = dict()
        for idx, n in enumerate(nums):
            if target - n not in num_map:
                num_map[n] = idx
            else:
                return [num_map[target - n], idx]

            class Solution(object):
                
                
 def twoSum(self, nums, target):
        i, j = 0, len(nums) - 1
        
        nums = [(idx, n) for idx, n in enumerate(nums)]
        nums.sort(key=lambda x: x[1])
        while i < j:
            value = nums[i][1] + nums[j][1] 
            if value == target:  
                return [nums[i][0], nums[j][0]]
            elif value > target:
                j -=1 
            else:
                i += 1

# class Solution:
#     def twoSum(self, nums, target):
#         """
#         Hash, O(N)
#         ---
#         1. Substracting the target with the currnt value
#         2. test if it has already existed in the dict; if not, do insertion
#         """
#         N = len(nums)
#         num_dict = dict()
#         for i in range(0, N):
#             tmp = target - nums[i]
#             if tmp in num_dict:
#                 return [num_dict[tmp], i]
#             else:
#                 num_dict[nums[i]] = i


# solution 2
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         Brutal Force, O(N^2)
#         """
#         N = len(nums)
#         for i in range(0, N):
#             for j in range(i+1, N):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
