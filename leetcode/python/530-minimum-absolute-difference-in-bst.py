'''
Online Compute the min
'''

class Solution(object):
    def getMinimumDifference(self, root):
        self.prev = 99999
        self.min_val = 99999
        self.inorder(root)
        return self.min_val
        
    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        self.min_val = min(self.min_val, abs(root.val-self.prev))
        self.prev = root.val
        if root.right:
            self.inorder(root.right)
        
        
'''
Acquire sorted array by inorder yraversal.
'''
# class Solution(object):
#     def getMinimumDifference(self, root):
#         self.c = []
#         self.inorder(root)
#         diff = [self.c[i] - self.c[i-1] for i in range(1, len(self.c))]
#         return min(diff)
        
#     def inorder(self, root):
#         if root is None:
#             return
#         self.inorder(root.left)
#         self.c.append(root.val)
#         self.inorder(root.right)
        
        
            