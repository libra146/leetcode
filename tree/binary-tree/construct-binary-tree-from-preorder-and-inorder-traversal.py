from typing import Optional, List

from utils import TreeNode


class Solution:
    m = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for index, a in enumerate(inorder):
            self.m[a] = index
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, p_start, p_end, inorder, i_start, i_end):
        if p_start > p_end:
            return
        root = TreeNode(preorder[p_start])
        index = self.m[root.val]
        left_size = index - i_start
        root.left = self.build(preorder, p_start + 1, p_start + left_size, inorder, i_start, index - 1)
        root.right = self.build(preorder, p_start + left_size + 1, p_end, inorder, index + 1, i_end)
        return root
