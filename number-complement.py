# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ ((1 << (len(bin(num)) - 2)) - 1)
# leetcode submit region end(Prohibit modification and deletion)
