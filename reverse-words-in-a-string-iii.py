# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for a in s.split():
            aa = list(a)
            aa.reverse()
            res.append(''.join(aa))
        return ' '.join(res)
# leetcode submit region end(Prohibit modification and deletion)
