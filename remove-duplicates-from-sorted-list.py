from typing import Optional

from utils.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow, fast = head, head.next
        while fast:
            if slow.val == fast.val:
                fast = fast.next
            elif slow.val != fast.val:
                slow.next = fast
                fast = fast.next
                slow = slow.next
        slow.next = None
        return head

# leetcode submit region end(Prohibit modification and deletion)
