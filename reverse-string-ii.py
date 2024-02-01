# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        r = []
        for index, a in enumerate(s):
            if index % (2 * k) == 0:
                rr = r[:k]
                rr.reverse()
                res.extend(rr)
                res.extend(r[k:])
                r.clear()
            r.append(a)
        rr = r[:k]
        rr.reverse()
        res.extend(rr)
        res.extend(r[k:])
        return ''.join(res)
# leetcode submit region end(Prohibit modification and deletion)
