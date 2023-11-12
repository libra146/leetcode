from typing import Optional

from utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.map = {0: 0}
        self.traverse(self.root)

    def traverse(self, root):
        if not root:
            return
        if root.left:
            self.map[2 * root.val + 1] = 0
            root.left.val = 2 * root.val + 1
        if root.right:
            self.map[2 * root.val + 2] = 0
            root.right.val = 2 * root.val + 2
        self.traverse(root.left)
        self.traverse(root.right)

    def find(self, target: int) -> bool:
        return self.map.get(target) is not None

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# leetcode submit region end(Prohibit modification and deletion)
