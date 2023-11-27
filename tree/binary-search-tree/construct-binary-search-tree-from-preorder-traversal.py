from typing import List, Optional

from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        for a in preorder:
            root = self.build(root, a)
        return root

    def build(self, root, val):
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.build(root.left, val)
        else:
            root.right = self.build(root.right, val)
        return root


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().bstFromPreorder([4, 2]))
