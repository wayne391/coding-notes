class Solution:
    def postorder(self, root) -> List[int]:
        if root is None:
            return []
        
        self.ans = []
        def traverse(root):
            for c in root.children:
                if c:
                    traverse(c)
            self.ans.append(root.val)
            
        traverse(root)
        return self.ans