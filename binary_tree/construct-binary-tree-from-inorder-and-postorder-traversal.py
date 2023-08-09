from typing import List, Optional

from utils import TreeNode


class Solution:
    m = {}

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        for index, a in enumerate(inorder):
            self.m[a] = index

        return self.build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def build(self, inorder, i_start, i_end, postorder, p_start, p_end):
        if i_start > i_end:
            return
        index = self.m[postorder[p_end]]
        left_size = index - i_start
        root = TreeNode(postorder[p_end])
        # p_start + left_size这里要 -1，因为使用了最后一个数，所有的索引往前移动 1
        root.left = self.build(inorder, i_start, index - 1, postorder, p_start, p_start + left_size - 1)
        # 这里也是一样，p_end 也要 -1
        root.right = self.build(inorder, index + 1, i_end, postorder, p_start + left_size, p_end - 1)
        return root
