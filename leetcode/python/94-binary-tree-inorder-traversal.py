def traverse(root, result):
    if not root:
        return
    traverse(root.left, result)
    result.append(root.val)
    traverse(root.right, result)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        result = []
        traverse(root, result)
        return result
