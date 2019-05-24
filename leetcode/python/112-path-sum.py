class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        self.sum = sum
        return self.dfs(root, 0) if root else False
        
    def dfs(self, cur_note, prev_sum):
        cur_sum = prev_sum + cur_note.val
        
        if not (cur_note.left or cur_note.right): 
            return cur_sum == self.sum
        
        flag_left = self.dfs(cur_note.left, cur_sum) if cur_note.left else False
        flag_right = self.dfs(cur_note.right, cur_sum) if cur_note.right else False

        return flag_left or flag_right