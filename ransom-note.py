# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for a in magazine:
            d[a] = d.get(a, 0) + 1
        for a in ransomNote:
            d[a] = d.get(a, 0) - 1
        return all(v >= 0 for v in d.values())
# leetcode submit region end(Prohibit modification and deletion)
