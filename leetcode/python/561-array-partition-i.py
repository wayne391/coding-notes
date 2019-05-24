class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
            
'''
Counting Sort
'''
# class Solution(object):
#     def arrayPairSum(self, nums):
#         N = len(nums)
#         table = [0 for _ in range(20001)]
#         for n in nums:
#             table[n+10000] += 1
#         sum_ = 0
#         i = 0
#         flag = True
#         while N > 0:
#             while table[i] == 0:
#                 i+=1
#             if flag:
#                 sum_ += (i-10000)
#                 flag = False
#             else:
#                 flag = True
#             table[i] -= 1
#             N -= 1
#         return sum_