import string


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        index = {a: string.ascii_uppercase.index(a) + 1 for a in string.ascii_uppercase}
        return sum(index[c] * 26 ** i for i, c in enumerate(reversed(columnTitle)))
# leetcode submit region end(Prohibit modification and deletion)
