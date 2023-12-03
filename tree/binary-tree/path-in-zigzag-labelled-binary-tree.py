from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        while label >= 1:
            res.append(label)
            t = label // 2
            label = t
        res.reverse()
        for index in range(len(res)):
            if index % 2 == len(res) % 2 and index != len(res) - 1 and index != 0:
                res[index] = pow(2, index + 1) - 1 - (res[index] - pow(2, index))
        return res
# leetcode submit region end(Prohibit modification and deletion)
