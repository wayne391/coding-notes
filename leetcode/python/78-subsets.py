'''
* best  solution
-----------------
[[]] (+1)
[[], [1]] (+ 2)
[[], [1], [2], [1, 2]] (+3)
[[], [1], [2], [3], [1, 2], [1, 3], [1, 2, 3]] (Done!)
Key: add new item for each existed element
'''


class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for n in nums:
            result = result + [r + [n] for r in result]
        return result


'''
* DFS
-----------------
                [ ]
             /    |   \
          [1]    [2]  [3]
         /  |     |
    [1, 2] [1, 3] [2, 3]
      /
[1, 2, 3]
'''


# class Solution(object):
#     def subsets(self, nums):
#         self.nums = nums
#         self.N = len(nums)
#         self.collect = [[]]
#         self.dfs(0, [])
#         return self.collect

#     def dfs(self, idx, sub):
#         for i in range(idx, self.N):
#             sub.append(self.nums[i])
#             self.collect = self.collect + [sub[:]]
#             self.dfs(i+1, sub)
#             sub.pop()
