from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root

    def traverse(self, root):
        if not root:
            return
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        root.left, root.right = right, left
        return root

# leetcode submit region end(Prohibit modification and deletion)
