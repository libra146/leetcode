from typing import List, Optional

from utils import TreeNode


class Solution:
    def __init__(self):
        self.res = []

    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.traverse(root, voyage)
        return self.res

    def traverse(self, root, voyage):
        if not root:
            return
        if -1 in self.res:
            return
        value = voyage.pop(0)
        if root.val != value:
            self.res.clear()
            self.res.append(-1)
            return
        if root.left and root.left.val != voyage[0]:
            self.res.append(root.val)
            root.left, root.right = root.right, root.left
        self.traverse(root.left, voyage)
        self.traverse(root.right, voyage)
