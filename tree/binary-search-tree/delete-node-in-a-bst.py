from typing import Optional

from utils import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key == root.val:
            if root.left is None:
                ###
                return root.right
            if root.right is None:
                return root.left
            # 取右子树的最小节点
            r = self.get_min(root.right)
            # 删除右子树的最小节点
            r.right = self.deleteNode(root.right, r.val)
            # 下面不能在deleteNode前赋值，不然上面的###就会返回错误的节点
            r.left = root.left
            root = r
        return root

    def get_min(self, node):
        # 取最小值，如果是右节点的话，左侧的值最小
        while node.left:
            node = node.left
        return node
