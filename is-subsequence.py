# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        if len(s) > len(t):
            return False
        fast, slow = 0, 0
        while fast < len(t) and slow < len(s):
            if s[slow] == t[fast]:
                slow += 1
            fast += 1
        return slow == len(s)
# leetcode submit region end(Prohibit modification and deletion)
