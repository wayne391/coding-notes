class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left if root.val > val else root.right, val)
