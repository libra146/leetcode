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
        self.res = {}

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root, 0, 0)
        result = []
        for a in sorted(self.res.items(), key=lambda x: x[0]):
            values = []
            for b in sorted(a[1].items(), key=lambda x: x[0]):
                b[1].sort()
                values.extend(b[1])
            result.append(values)
        return result

    def traverse(self, root, r, c):
        if not root:
            return
        if c not in self.res:
            self.res[c] = {r: [root.val]}
        else:
            if r not in self.res[c]:
                self.res[c][r] = [root.val]
            else:
                self.res[c][r].append(root.val)
        self.traverse(root.left, r + 1, c - 1)
        self.traverse(root.right, r + 1, c + 1)

# leetcode submit region end(Prohibit modification and deletion)
