from typing import Optional

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

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 1)]
        while q:
            current = []
            for node, index in q:
                if node.left:
                    current.append((node.left, 2 * index))
                if node.right:
                    current.append((node.right, 2 * index + 1))
                self.res = max(self.res, q[-1][1] - q[0][1] + 1)
            q = current
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
