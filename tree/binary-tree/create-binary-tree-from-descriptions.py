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
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        r = {}
        p_root = set()
        for p, c, i in descriptions:
            p_root.add(c)
            if p in r:
                if i == 0:
                    r[p][1] = c
                else:
                    r[p][0] = c
            else:
                if i == 0:
                    r[p] = [None, c]
                else:
                    r[p] = [c, None]
        root = set(r.keys()) - p_root
        return self.build(root.pop(), r)

    def build(self, root_val, r):
        if not root_val:
            return
        if root_val in r:
            root = TreeNode(root_val)
            left, right = r.pop(root_val)
            root.left = self.build(left, r)
            root.right = self.build(right, r)
            return root
        else:
            return TreeNode(root_val)
# leetcode submit region end(Prohibit modification and deletion)
