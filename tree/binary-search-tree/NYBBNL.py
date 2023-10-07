from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.new_root = None
        self.res = None

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.increasingBST(root.left)
        if self.new_root is None:
            self.new_root = TreeNode(root.val)
            self.res = self.new_root
        else:
            self.new_root.right = TreeNode(root.val)
            self.new_root = self.new_root.right
        self.increasingBST(root.right)
        return self.res
# leetcode submit region end(Prohibit modification and deletion)
