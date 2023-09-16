from typing import List, Optional

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
        self.res = None
        self.height = 0

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        self.height = self.parse_height(root) - 1
        self.res = [["" for _ in range(pow(2, self.height + 1) - 1)] for _ in range(self.height + 1)]
        self.res[0][(pow(2, self.height + 1) - 1 - 1) // 2] = str(root.val)
        self.traverse(root, 0, (pow(2, self.height + 1) - 1 - 1) // 2)
        return self.res

    def traverse(self, root: Optional[TreeNode], r, c):
        q = [(root, r, c)]
        while q:
            q_len = len(q)
            for a in range(q_len):
                node, r, c = q.pop(0)
                if node.left:
                    self.res[r + 1][c - pow(2, self.height - r - 1)] = str(node.left.val)
                    q.append((node.left, r + 1, c - pow(2, self.height - r - 1)))
                if node.right:
                    self.res[r + 1][c + pow(2, self.height - r - 1)] = str(node.right.val)
                    q.append((node.right, r + 1, c + pow(2, self.height - r - 1)))

    def parse_height(self, root: Optional[TreeNode]):
        if not root:
            return 0
        return max(self.parse_height(root.left), self.parse_height(root.right)) + 1
# leetcode submit region end(Prohibit modification and deletion)
