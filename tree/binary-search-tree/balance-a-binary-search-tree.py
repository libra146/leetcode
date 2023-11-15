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
        self.res = []

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        print(self.res)
        return self.build(0, len(self.res) - 1)

    def build(self, l, r):
        if l > r:
            return
        root_index = (l + r) // 2
        root = TreeNode(self.res[root_index])
        root.left = self.build(l, root_index - 1)
        root.right = self.build(root_index + 1, r)
        return root

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)
# leetcode submit region end(Prohibit modification and deletion)
