from utils import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.traverse(root)[0]

    def traverse(self, root):
        if not root:
            return None, 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        if left[1] == right[1]:
            return root, right[1] + 1
        else:
            if left[1] > right[1]:
                return left[0], left[1] + 1
            else:
                return right[0], right[1] + 1
