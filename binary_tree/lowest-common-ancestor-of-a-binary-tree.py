from utils import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        l = self.lowestCommonAncestor(root.left, q, p)
        r = self.lowestCommonAncestor(root.right, q, p)
        if l is not None and r is not None:
            return root
        return l if l is not None else r
