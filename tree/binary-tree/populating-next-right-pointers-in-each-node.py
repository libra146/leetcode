from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return
        q = [root]
        while q:
            size = len(q)
            pre = None
            for _ in range(size):
                n = q.pop(0)
                if pre is None:
                    pre = n
                else:
                    pre.next = n
                    pre = n
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return root


class Solution2:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return
        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1, node2):
        if not node2:
            return
        node1.next = node2
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        self.traverse(node1.right, node2.left)
