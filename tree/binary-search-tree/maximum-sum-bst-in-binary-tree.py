from typing import Optional, List

from utils import TreeNode


class Solution:
    def __init__(self):
        self.max_value = 0

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # traverse(root)返回一个大小为 4 的 int 数组，我们暂且称它为res，其中：
        # res[0]记录以root为根的二叉树是否是 BST，若为 1 则说明是 BST，若为 0 则说明不是 BST；
        # res[1]记录以root为根的二叉树所有节点中的最小值；
        # res[2]记录以root为根的二叉树所有节点中的最大值；
        # res[3]记录以root为根的二叉树所有节点值之和。
        self.traverse(root)
        return self.max_value

    def traverse(self, node: Optional[TreeNode]) -> List[int]:
        if not node:
            return [1, float('inf'), float('-inf'), 0]
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        res = [1, float('inf'), float('-inf'), 0]
        if left[0] == 1 and right[0] == 1 and left[2] < node.val < right[1]:
            res[0] = 1
            res[1] = min(left[1], node.val)
            res[2] = max(right[2], node.val)
            res[3] = node.val + left[3] + right[3]
            self.max_value = max(self.max_value, res[3])
        else:
            res[0] = 0
        return res
