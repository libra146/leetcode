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
        self.res = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return 0
        if root.val % 2 == 0:
            if root.left:
                if root.left.left:
                    self.res += root.left.left.val
                if root.left.right:
                    self.res += root.left.right.val
            if root.right:
                if root.right.left:
                    self.res += root.right.left.val
                if root.right.right:
                    self.res += root.right.right.val
        self.traverse(root.left)
        self.traverse(root.right)

# leetcode submit region end(Prohibit modification and deletion)
