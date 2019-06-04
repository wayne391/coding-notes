class Solution(object):
    def sortColors(self, nums):
        cur = 0
        head = 0
        tail = len(nums) - 1
        while cur <= tail:
            if nums[cur] == 2:
                nums[tail], nums[cur] = nums[cur], nums[tail]
                tail -= 1
            elif nums[cur] == 0:
                nums[head], nums[cur] = nums[cur], nums[head]
                head += 1
                cur += 1
            else:
                cur += 1
        return nums