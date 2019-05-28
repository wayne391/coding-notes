class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        val_left = self.maxDepth(root.left) if root.left else 0
        val_right = self.maxDepth(root.right) if root.right else 0
        return max(val_left, val_right) + 1

'''
O
'''
def maxDepth(self, root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0