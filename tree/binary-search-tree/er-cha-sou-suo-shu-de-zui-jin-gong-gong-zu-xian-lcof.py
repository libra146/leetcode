from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traverse(root, p, q)

    def traverse(self, root, p, q):
        if not root:
            return
        if root.val == p.val or root.val == q.val:
            return root
        left = self.traverse(root.left, p, q)
        right = self.traverse(root.right, p, q)
        if left and right:
            return root
        return left if left else right
# leetcode submit region end(Prohibit modification and deletion)
