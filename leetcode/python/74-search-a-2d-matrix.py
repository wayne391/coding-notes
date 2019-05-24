class Solution:
    def searchIndex(self, nums, target):
        low, high = 0, len(nums)
        while(low < high):
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return None

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sorted_list = []
        for row in matrix:
            sorted_list += row

        return self.searchIndex(sorted_list, target) != None
