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
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.traverse(root, val)

    def traverse(self, root, val):
        if not root:
            return
        if root.val < val:
            new_node = TreeNode(val, left=root)
            root = new_node
        else:
            if root.right:
                if root.right.val > val:
                    root.right = self.traverse(root.right, val)
                else:
                    root.right = TreeNode(val, left=root.right)
            else:
                root.right = TreeNode(val)
        return root
# leetcode submit region end(Prohibit modification and deletion)
