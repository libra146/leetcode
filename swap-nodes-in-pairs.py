from typing import Optional

from utils.ListNode import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fast = head.next
        new = fast
        slow = head
        pre = None
        while fast:
            tmp = fast.next
            fast.next = slow
            slow.next = tmp
            if pre:
                pre.next = fast
            if not tmp or not tmp.next:
                break
            pre = fast.next
            fast = tmp.next
            slow = tmp
        return new
# leetcode submit region end(Prohibit modification and deletion)
