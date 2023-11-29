from typing import Optional

from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            self.res = 0
            for a in range(len(queue)):
                node = queue.pop(0)
                self.res += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return self.res
# leetcode submit region end(Prohibit modification and deletion)
