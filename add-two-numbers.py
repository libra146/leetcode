from typing import Optional

from utils.ListNode import ListNode


class Solution:
    def __init__(self):
        self.head = None
        self.current = None
        self.j = False

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 进位
        self.j = False
        self.head = None
        self.current = self.head
        while l2 or l1:
            if l1 is not None and l2 is not None:
                self.add(l1.val + l2.val + (1 if self.j else 0))
            else:
                if l1:
                    self.add(l1.val + (1 if self.j else 0))
                if l2:
                    self.add(l2.val + (1 if self.j else 0))
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if self.j:
            self.add(1)
        return self.head

    def add(self, val):
        if val >= 10:
            value = val - 10
            self.j = True
        else:
            value = val
            self.j = False
        if self.head is None:
            self.head = ListNode(val=value)
            self.current = self.head
        else:
            self.current.next = ListNode(val=value)
            self.current = self.current.next


class SolutionRecursion(object):
    # 递归版本，参考其他人
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return ListNode(val=1) if carry else None
        if l1 is None:
            l1, l2 = l2, l1
        l1.val = l1.val + (l2.val if l2 else 0) + (1 if carry else 0)
        carry = l1.val // 10
        if carry == 1:
            l1.val = l1.val % 10
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, carry)
        return l1


if __name__ == '__main__':
    head = ListNode(val=9)
    current = head
    current.next = ListNode(val=9)
    current = current.next
    current.next = ListNode(val=9)
    current = current.next

    head2 = ListNode(val=9)
    print(head)
    print(head2)
    # print(Solution().addTwoNumbers(head, head))
    # print(Solution().addTwoNumbers(head, head2))
    print(SolutionRecursion().addTwoNumbers(head, head2))
