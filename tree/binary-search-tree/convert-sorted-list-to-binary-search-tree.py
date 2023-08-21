from typing import Optional

from utils import TreeNode
from utils.ListNode import ListNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, lo, hi):
        if lo > hi:
            return
        middle = lo + (hi - lo) // 2
        root = TreeNode(nums[int(middle)])
        root.left = self.build(nums, lo, middle - 1)
        root.right = self.build(nums, middle + 1, hi)
        return root


class Solution2:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return
        if head.next is None:
            return TreeNode(head.val)
        pre = None
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
