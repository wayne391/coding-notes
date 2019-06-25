class Solution:
    def preorder(self, root):
        if root is None:
            return []
        
        self.ans = []
        def traverse(root):
            self.ans.append(root.val)
            for c in root.children:
                if c:
                    traverse(c)
            
        traverse(root)
        return self.ans