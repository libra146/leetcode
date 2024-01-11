from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for a in operations:
            if a == '+':
                stack.append(stack[-1] + stack[-2])
                continue
            if a == 'D':
                stack.append(stack[-1] * 2)
                continue
            if a == 'C':
                stack.pop()
                continue
            else:
                stack.append(int(a))
        return sum(stack)
# leetcode submit region end(Prohibit modification and deletion)
