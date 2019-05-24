
'''
While loop.
'''

class Solution(object):
    def searchInsert(self, nums, target):
        low, high = 0, len(nums)-1
        while(low <= high):
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low

'''
Exclude high
'''

# class Solution(object):
#     def searchInsert(self, nums, target):
#         low, high = 0, len(nums)
#         while(low < high):
#             mid = (high+low)//2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 high = mid
#             else:
#                 low = mid + 1
#         return low

'''
My original recursion version. Consume more memory
'''
# class Solution(object):
#     def searchInsert(self, nums, target):
#         N = len(nums)
#         mid = N // 2 
#         if N == 1:
#             return 1 if target > nums[mid] else 0
#         if target < nums[mid]:
#             return self.searchInsert(nums[:mid], target)
#         else:
#             return (mid) + self.searchInsert(nums[mid:], target)
'''
Theoritically O(n), but amazingly fast.
'''
# class Solution(object):
#     def searchInsert(self, nums, target):
#         for i in range(len(nums)):
#             if nums[i] >= target:
#                 return i
#         return len(nums)    