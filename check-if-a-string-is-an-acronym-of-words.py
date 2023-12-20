from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return ''.join([word[0] for word in words]) == s

# leetcode submit region end(Prohibit modification and deletion)
