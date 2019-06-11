class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        N = len(nums)
        nums.sort()
        
        def dfs(start, path):
            if start >= N:
                return
            prev = None
            for i in range(start, N):
                if nums[i] == prev:
                    continue
                else:
                    prev = nums[i]
                    temp = path + [nums[i]]
                    res.append(temp)
                    dfs(i + 1, temp)
        
        dfs(0, [])
        return res
            