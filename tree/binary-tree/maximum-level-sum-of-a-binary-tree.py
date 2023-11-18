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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result = float('inf')
        res = float('-inf')
        level = 0
        queue = [root]
        while queue:
            level += 1
            sum_ = 0
            l = len(queue)
            for a in range(l):
                node = queue.pop(0)
                sum_ += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum_ > res:
                res = sum_
                result = level
        return result
# leetcode submit region end(Prohibit modification and deletion)
