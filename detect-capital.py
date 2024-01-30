# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word or word.lower() == word or word.capitalize() == word:
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
