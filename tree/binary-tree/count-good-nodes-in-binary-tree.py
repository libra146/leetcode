from utils import TreeNode


class Solution:
    def __init__(self):
        self.res = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root, root.val)
        return self.res

    def traverse(self, node, max_val):
        if not node:
            return
        if node.val >= max_val:
            self.res += 1
        if node.left:
            self.traverse(node.left, max(node.val, max_val))
        if node.right:
            self.traverse(node.right, max(node.val, max_val))
