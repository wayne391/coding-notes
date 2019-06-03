'''
Queue Solution
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        queue = [root.left, root.right]

        while len(queue):
            a = queue.pop(0)
            b = queue.pop(0)
            
            if bool(a) != bool(b):
                return False
            if a is None:
                continue
            if a.val != b.val:
                return False
            queue.extend([a.left, b.right, a.right, b.left])
        return True

'''
Recursion Solution
'''
def is_mirror(a, b):
    if  bool(a) != bool(b):
        return False
    if a is None:
        return True
    if a.val != b.val:
        return False
    res_a = is_mirror(a.left, b.right)
    res_b = is_mirror(a.right, b.left)
    return res_a and res_b

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return is_mirror(root.left, root.right)