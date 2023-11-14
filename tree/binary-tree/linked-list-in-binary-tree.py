from typing import Optional

from utils import TreeNode, ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.traverse(head, root)

    def dfs(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        if head.val == root.val:
            return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)
        else:
            return False

    def traverse(self, head, root):
        if not head:
            return True
        if not root:
            return False
        if self.dfs(head, root):
            return True
        return self.traverse(head, root.left) or self.traverse(head, root.right)
# leetcode submit region end(Prohibit modification and deletion)
