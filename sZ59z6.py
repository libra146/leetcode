from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def numColor(self, root: TreeNode) -> int:
        self.res = set()
        self.traverse(root)
        return len(self.res)

    def traverse(self, root):
        if not root:
            return
        self.res.add(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

# leetcode submit region end(Prohibit modification and deletion)
