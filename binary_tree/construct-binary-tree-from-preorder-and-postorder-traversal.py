from typing import List, Optional

from utils import TreeNode


class Solution:
    m = {}

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        for index, a in enumerate(postorder):
            self.m[a] = index
        return self.build(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)

    def build(self, preorder, pre_start, pre_end, postorder, po_start, po_end):
        if pre_start > pre_end:
            return
        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])
        root_value = preorder[pre_start]
        index = self.m[preorder[pre_start + 1]]
        left_size = index - po_start + 1
        root = TreeNode(root_value)
        root.left = self.build(preorder, pre_start + 1, pre_start + left_size, postorder, po_start, index)
        root.right = self.build(preorder, pre_start + left_size + 1, pre_end, postorder, index + 1, po_end - 1)
        return root
