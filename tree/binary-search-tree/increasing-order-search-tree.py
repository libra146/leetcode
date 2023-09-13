from utils import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        node = TreeNode(-1)
        self.res = node
        self.traverse(root)
        return node

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        if self.res.val == -1:
            self.res.val = root.val
        else:
            self.res.right = TreeNode(root.val)
            self.res = self.res.right
        self.traverse(root.right)
