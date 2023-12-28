from typing import Optional

from utils.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if not head:
            return
        p = head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
