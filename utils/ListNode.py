class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        r = [str(self.val)]
        c = self
        while c.next:
            c = c.next
            r.append(str(c.val))
        return '->'.join(r)
