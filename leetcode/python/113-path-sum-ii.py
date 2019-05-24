'''
My Solution  87.18% in time &  43.20% in space
'''
class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        self.sum = sum
        self.collect = []
        if root:
            self.dfs(root, 0, [])
        return self.collect
        
    def dfs(self, cur_note, prev_sum, subList):
        if cur_note is None:
            return
        
        cur_sum = prev_sum + cur_note.val
        new_sub = subList+[cur_note.val]
        
        if not (cur_note.left or cur_note.right) and cur_sum == self.sum: 
            self.collect.append(new_sub)
        
        self.dfs(cur_note.left, cur_sum, new_sub)
        self.dfs(cur_note.right, cur_sum, new_sub)

'''
From discussion, caikehe:  98.19% in time & 69.09% in space
'''

# class Solution:
#     def pathSum(self, root, sum):
#         if not root:
#             return []
#         if not (root.left or root.right) and sum == root.val:
#             return [[root.val]]
#         tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
#         return [[root.val]+i for i in tmp]
