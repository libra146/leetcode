class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
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
