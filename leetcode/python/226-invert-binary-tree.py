class Solution(object):
    def invertTree(self, root):
        if root is None:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp
        return root
        