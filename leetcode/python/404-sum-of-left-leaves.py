class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.sum = 0
        self.go_left = False
        self.traverse(root)
        return self.sum
    
    def traverse(self, root):
        if root is None:
            return
        
        if not (root.left or root.right):
            if self.go_left:
                self.sum += root.val
                return 
            
        self.go_left = True
        self.traverse(root.left)
        self.go_left = False
        self.traverse(root.right)


# class Solution(object):
#     def sumOfLeftLeaves(self, root):
#         return self.traverse(root)
    
#     def traverse(self, root):
#         if root is None:
#             return 0
#         if root.left and not(root.left.left or root.left.right):
#             return root.left.val + self.traverse(root.right)
#         return self.traverse(root.left) + self.traverse(root.right)