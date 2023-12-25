# leetcode submit region begin(Prohibit modification and deletion)
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        node = self.peek()
        self.s2.pop(0)
        return node

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                node = self.s1.pop(0)
                self.s2.append(node)
        return self.s2[0] if self.s2 else None

    def empty(self) -> bool:
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)
