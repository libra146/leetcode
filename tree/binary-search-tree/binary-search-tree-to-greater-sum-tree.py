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

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.right)
        self.res.append(root.val)
        root.val = sum(self.res)
        self.dfs(root.left)

# leetcode submit region end(Prohibit modification and deletion)
