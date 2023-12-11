from typing import Optional

from utils.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        h = ListNode(head.val)
        n = None
        while head.next:
            n = ListNode(head.next.val)
            n.next = h
            h = n
            head = head.next
        return n or h
# leetcode submit region end(Prohibit modification and deletion)
