def check_path(root):
    (left_sum, left_path) = check_path(root.left) if root.left else (0, -1)
    (right_sum, right_path) = check_path(root.right) if root.right else (0, -1)
    left_path += 1
    right_path += 1
    return max(left_sum, right_sum, left_path + right_path), max(left_path, right_path)

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return check_path(root)[0] if root else 0
        