from typing import List

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

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.traverse(root1)
        self.traverse(root2)

        return sorted(self.res)

    def traverse(self, root):
        if not root:
            return
        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

# leetcode submit region end(Prohibit modification and deletion)
