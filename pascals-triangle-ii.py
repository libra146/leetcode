from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.res = []

    def getRow(self, rowIndex: int) -> List[int]:
        return self.generate(rowIndex)

    def generate(self, index):
        if index == 0:
            self.res = [1]
            return self.res
        if index == 1:
            self.res = [1, 1]
            return self.res
        self.generate(index - 1)
        t = [1]
        for a in range(0, len(self.res) - 1):
            t.append(self.res[a] + self.res[a + 1])
        t.append(1)
        self.res = t
        return self.res
# leetcode submit region end(Prohibit modification and deletion)
