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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        level = 0
        while queue:
            sum_ = 0
            for a in range(len(queue)):
                node = queue.pop(0)
                if not node:
                    continue
                queue.append(node.left)
                queue.append(node.right)
                sum_ += node.left.val if node.left else 0
                sum_ += node.right.val if node.right else 0
                if level < 2:
                    node.val = 0
                    continue
            level += 1
            for index in range(0, len(queue), 2):
                s = (queue[index].val if queue[index] else 0) + (queue[index + 1].val if queue[index + 1] else 0)
                if queue[index]:
                    queue[index].val = sum_ - s
                if queue[index + 1]:
                    queue[index + 1].val = sum_ - s
        return root
# leetcode submit region end(Prohibit modification and deletion)
