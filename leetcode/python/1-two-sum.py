class Solution(object):
    def twoSum(self, nums, target):
        num_map = dict()
        for idx, n in enumerate(nums):
            if target - n not in num_map:
                num_map[n] = idx
            else:
                return [num_map[target - n], idx]


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
