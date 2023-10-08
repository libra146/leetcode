from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.pre = None

    def convertBiNode(self, root: TreeNode) -> TreeNode:
        node = TreeNode()
        self.pre = node
        self.traverse(root)
        return node.right

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.pre.right = root
        self.pre.right.left = None
        self.pre = root
        self.traverse(root.right)
# leetcode submit region end(Prohibit modification and deletion)
