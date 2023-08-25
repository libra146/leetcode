from typing import Optional

from utils import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.val = None
        self.tr = self.traverse(root)

    def next(self) -> int:
        if self.hasNext():
            val = self.val
            self.val = None
            return val

    def traverse(self, node):
        if not node:
            return
        yield from self.traverse(node.left)
        yield node.val
        yield from self.traverse(node.right)

    def hasNext(self) -> bool:
        if self.val is not None:
            return True
        try:
            self.val = next(self.tr)
            return True
        except StopIteration:
            return False


class BSTIterator2:
    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.queue = []
        # 将根节点和所有的左节点入栈
        while self.cur:
            self.queue.append(self.cur)
            self.cur = self.cur.left

    def next(self) -> int:
        node = self.queue.pop()
        self.cur = node.right
        while self.cur:
            self.queue.append(self.cur)
            self.cur = self.cur.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.queue) > 0
