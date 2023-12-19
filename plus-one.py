from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        res = []
        one = True
        for a in digits[::-1]:
            if one:
                s = a + 1
                one = False
            else:
                s = a
            if carry:
                s = a + 1
                carry = 0
            if s >= 10:
                carry = 1
                s = s - 10
            res.insert(0, s)
        if carry == 1:
            res.insert(0, 1)
        return res
# leetcode submit region end(Prohibit modification and deletion)
