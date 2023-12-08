from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for a in range(3, numRows + 1):
            t = res[-1]
            rr = [1]
            for b in range(0, len(t) - 1):
                rr.append(t[b] + t[b + 1])
            rr.append(1)
            res.append(rr)
        return res
# leetcode submit region end(Prohibit modification and deletion)
