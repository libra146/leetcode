from typing import Optional

from utils import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = root.left
        l_count = 0
        while l:
            l_count += 1
            l = l.left
        r = root.right
        r_count = 0
        while r:
            r_count += 1
            r = r.right
        if l_count == r_count:
            return 2 ** l_count - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


class Solution2:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = root
        l_count = 0
        while l:
            l_count += 1
            l = l.left
        r = root
        r_count = 0
        while r:
            r_count += 1
            r = r.right
        if l_count == r_count:
            return 2 ** l_count - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
